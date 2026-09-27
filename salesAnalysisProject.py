from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()



conn = connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)


print("Connected..")


cur=conn.cursor()

def show_products():
    cur.execute("Select * from product")
    all_products=cur.fetchall()
    for i in all_products:
        print("-"*106)
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]} | {i[6]}")

def search_products():
    p_name=input("Enter Product Name ")
    cur.execute("select * from product where product_name=%s",(p_name,))
    pr=cur.fetchall()
    for data in pr:
        print(f'''
                  Product Id:     {data[0]} 
                  Product Name:   {data[1]} 
                  Category:       {data[2]} 
                  Price:          {data[3]} 
                  Quantity Sold:  {data[4]}''')

def calculate_total_sales():
    cur.execute("select * from product")
    total=0
    for all_data in cur.fetchall():
        price=all_data[3]
        quantity=all_data[4]
        sales_amount=price*quantity
        total=total+sales_amount
        print(f'''
              Product Category: {all_data[2]}
              Sales Amount:    {sales_amount}
              ''')  
    print(f'''Total Sales: {total}''')

def highest_quantity_sold():
    cur.execute("select product_name,quantity_sold from product  where quantity_sold=(SELECT MAX(quantity_sold) FROM product)")
    for data in cur.fetchall():
        print(f''' 
                    Product Name: {data[0]}
                    Highest Quantity Sold: {data[1]}''')

def highest_revenue():
     cur.execute("select product_name, price*quantity_sold as revenue from product where price*quantity_sold=(select max(price*quantity_sold) from product);")
     for all_data in cur.fetchall():
            print(all_data)

def category_wise_analysis():
    cur.execute("select category,count(*),sum(quantity_sold), sum(price*quantity_sold) from product group by category")
    for data in cur.fetchall():
        print(f'''
              Category          :  {data[0]}
              Total Product     :  {data[1]}
              Sold Quantity     :  {data[2]}
              Total Revenue     :  {data[3]}''')

def city_wise_analysis():
    cur.execute("select city, sum(price*quantity_sold) from product group by city;")
    for data in cur.fetchall():
        print(f'''
              City: {data[0]}
              Revenue: {data[1]}''')

def total_discount():
    cur.execute("select sum(price*quantity_sold*discount/100) as total_discount from product")
    for dis in cur.fetchall():
        print(dis)

def low_sales_products():
    cur.execute("select * from product where quantity_sold<20")
    low_sales=cur.fetchall()
    
    for data in low_sales:
        price=data[3]
        discount=data[5]
        quantity_sold=data[4]
        
        revenue=price*quantity_sold
        discount_amount=revenue*discount/100
        net_revenue=revenue-discount_amount
        
        print(f'''
        ---------------------------
        Product Name    :{data[1]} 
        Quantity Sold   :{quantity_sold}
        Revenue         :{revenue}
        Discount Amount :{discount_amount}
        Net Revenue     :{net_revenue}
        ----------------------------
              ''')
        
        query=""" 
        insert ignore into product_analysis(product_name, revenue, discount_amount, net_revenue)
        values(%s,%s,%s,%s)
        """
        cur.execute(
            query,(data[1],revenue,discount_amount,net_revenue)
        )
    conn.commit()

while True:
    print('''
          1. Display All Products
          2. Search Product
          3. Calculate Total Sales
          4. Find Best Selling Products
          5. Find Highest Revenue Products
          6. Category-Wise Sales Analysis
          7. City-wise Sales Analysis
          8. Calculate Total Discount
          9. Find Products with low sales
          10. Exit''')
    try:
        choice=int(input("Enter Your choice: "))
    except ValueError:
        print("Please enter a valid number between 1 and 10.")
        continue
    if choice==1:
        show_products()
        
    elif choice==2:
        search_products()
    
    elif choice==3:
        calculate_total_sales()
    
    elif choice==4:
        highest_quantity_sold()
        
    elif choice==5:
        highest_revenue()
    
    elif choice==6:
        category_wise_analysis()
    
    elif choice==7:
        city_wise_analysis()
    
    elif choice==8:
        total_discount()
        
    elif choice==9:
        low_sales_products()
    
    elif choice==10:
        print("Thank You ")
        break
    else:
        print("Invalid Choice")

cur.close()
conn.close()
print("database connection closed")
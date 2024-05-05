import mysql.connector
import bcrypt


db_config = {
    "user": "root",
    "password": "3mm@hNj3r!",
    "host": "localhost",
    "database": "users",  
}


try:
    conn = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)


create_table_query = """
CREATE TABLE IF NOT EXISTS user_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alias VARCHAR(50),
    password BLOB,  
    is_admin BOOLEAN  
)
"""

with conn.cursor() as cursor:
    cursor.execute(create_table_query)
    conn.commit()


def register_user(alias, plain_password, is_admin=False):
    
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

    
    insert_query = """
    INSERT INTO user_info (alias, password, is_admin) 
    VALUES (%s, %s, %s)
    """
    
    with conn.cursor() as cursor:
        cursor.execute(insert_query, (alias, hashed_password, is_admin))
        conn.commit()



def verify_user(alias, plain_password):                                                                        
    # Fetch the stored hash from the database                                                                                        
    select_query = """                                                                                         
    SELECT password FROM user_info                     
    WHERE alias = %s                                   
    """                                                                                                        
                                                       
    with conn.cursor() as cursor:                                                                              
        cursor.execute(select_query, (alias,))                                                                                       
        user = cursor.fetchone()  # Get the first matching record                                                                                   
                                                                                                               
        if user:                                                                                                                     
            stored_hash = user[0]                                                                                                                   
                                                                  
            # Ensure stored_hash is in bytes                                                                   
            if isinstance(stored_hash, str):                      
                stored_hash = stored_hash.encode('utf-8')                                                                                                              
                                                                                                                                     
            # Encode the plaintext password                       
            if bcrypt.checkpw(plain_password.encode('utf-8'), stored_hash):                                                                                            
                print("Login successful!")                                                                                           
                return True                                                                                                                         
            else:                        
                print("Incorrect password!")                                       
                return False                                                       
        else:                            
            print("User not found.")                                               
            return False



def is_admin(alias):
    
    select_query = """
    SELECT is_admin FROM user_info 
    WHERE alias = %s
    """
    
    with conn.cursor() as cursor:
        cursor.execute(select_query, (alias,))
        user = cursor.fetchone()  
    
    if user:
        return user[0]  
    else:
        return False  


register_user("kratos", "3ll!0tAld3rs0n@95", is_admin=True)  
register_user("takishdnk", "kibenicky@20*+", is_admin=True)  


conn.close()

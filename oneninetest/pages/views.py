from django.shortcuts import render,redirect
import psycopg2
from accounts.models import Accounts
# Create your views here.


def login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        servername = request.POST['servername']
        server = Accounts.objects.all().filter(username=username, password=password, servername=servername)
        if server:
            server=server.values()[0]
            conn = psycopg2.connect(
                user=server['username'],
                password=server['password'],
                host='127.0.0.1',
                port='5432',
                database=server['servername']
            )
            cursor = conn.cursor()
            cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
            table_list=[]
            for row in cursor.fetchall(): 
               table_list.append(list(row)) 
            flat_list = [item for sublist in table_list for item in sublist]
            print(flat_list)
            context = {
                'tables':flat_list,
                'username':server['username'],
                'servername':server['servername'],
                'password':server['password']
            }
            return render(request,'tables.html',context)

        else:
            print('wrong credentials')
            return redirect('login')
    else:     
        return render(request,'login.html')

def tables(request):
    print('hi nigga')
    if request.method == 'POST':
        print(request.POST)
        table = request.POST['table']
        username = request.POST['username']
        password = request.POST['password']
        servername = request.POST['servername']
        print(table)
        conn = psycopg2.connect(
            user=username,
            password=password,
            host='127.0.0.1',
            port='5432',
            database=servername
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM '+table+' LIMIT 10')
        print(cursor)
        data_list=[]
        for row in cursor.fetchall(): 
            data_list.append(list(row)) 
        
        print(data_list)
        cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        table_list=[]
        for row in cursor.fetchall(): 
            table_list.append(list(row)) 
        
        flat_list = [item for sublist in table_list for item in sublist]
        print(flat_list)
        context ={
            'data':data_list,
            'tables':flat_list,
            'username':username,
            'servername':servername,
            'password':password
        }
        return render(request,'tables.html',context)
    else:
        return render(request,'tables.html')

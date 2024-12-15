

# Task 1 and Task2: Creating a Django-Based API

#               CONFIGURATIONS: 
first create the virtual environment :
        --> python -m venv .venv

then install django:
        --> pip install django

then start/make a project:
        --> django-admin startproject assignment

then app inside the project:
        --> python manage.py startapp api

then make configurations related to api app :
            Register the App in ****settings.py:
            Open assignments/settings.py and add 'api', to the INSTALLED_APPS list

            add app's url in the project's url file
                    path('apis/',include("api.urls"))



# #######----------assignment/api/urls.py file----------

from django.urls import path
from . import views

urlpatterns = [
    path('add-app/', views.add_app, name='add_app'),
    path('get-app/<int:id>/', views.get_app, name='get_app'),
    path('delete-app/<int:id>/', views.delete_app, name='delete_app'),
]

-------------------------------------------------------------------------

# ------------------------views.py-------------------------------------
integration with database:


import json
from django.http import JsonResponse
from .models import App

def add_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            app = App.objects.create(
                app_name=data['app_name'],
                version=data['version'],
                description=data['description']
            )
            return JsonResponse({'id': app.id, 'message': 'App added successfully!'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data format'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def get_app(request, id):
    try:
        app = App.objects.get(id=id)
        return JsonResponse({
            'id': app.id,
            'app_name': app.app_name,
            'version': app.version,
            'description': app.description
        })
    except App.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)

def delete_app(request, id):
    try:
        app = App.objects.get(id=id)
        app.delete()
        return JsonResponse({'message': 'App deleted successfully!'}, status=200)
    except App.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)


# --------------------------models.py-------------------------
#      database schema:


from django.db import models

class App(models.Model):
    app_name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.app_name

# --------------------------------------------------------       

then check and create table:
    python manage.py makemigrations
    python manage.py migrate

-----------------------------------------------------------------------------------------------------

# ----------------Run this django-api and its integration on localhost :--------------
        
                -->python manage.py runserver

                    Starting development server at http://127.0.0.1:8000/


# ######---add data----

curl -X POST http://127.0.0.1:8000/apis/add-app/ \
-H "Content-Type: application/json" \
-d '{"id":1 ,app_name": "MyApp", "version": "1.0", "description": "Sample app description."}'


we can also django admin gui interface
for this we have to register our app , for this open admin.py file:
    admin.site.register(App)

# #####------get data --------

curl http://127.0.0.1:8000/apis/get-app/2/

output:
{"id": 2, "app_name": "ChatGPT", "version": "1.0", "description": "An AI-based chatbot for conversations."}



# #####-------delete data--------------
curl -X DELETE http://127.0.0.1:8000/apis/delete-app/2/

output:
{"message": "App deleted successfully!"}

on server:
[15/Dec/2024 22:56:44] "DELETE /apis/delete-app/2/ HTTP/1.1" 200 40



# #######################   TASK 3  ##################################################
# TASK 3


# first i install android studio , then i use its android emulator and launch it using the below python script

# then i create an hellow world app on the android studio 
import subprocess
import os

# Path to the Android emulator executable
EMULATOR_PATH = "C:/Users/praneet_bawa/AppData/Local/Android/Sdk/emulator/emulator.exe"  
AVD_NAME = "Medium_Phone_API_35"  #(Android Virtual Device AVDID)
ADB_PATH = "C:/Users/praneet_bawa/AppData/Local/Android/Sdk/platform-tools/adb.exe"

def launch_android_emulator():
    try:
        subprocess.Popen([EMULATOR_PATH, "-avd", AVD_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Android Emulator is launching...")
    except FileNotFoundError:
        print("Error: Emulator executable not found. Please check the EMULATOR_PATH.")
    except Exception as e:
        print(f"Error: An error occurred: {str(e)}")

def install_apk(apk_path):
    if not os.path.exists(apk_path):
        print("Error: APK file not found.")
        return
    
    try:
# Wait for the emulator to boot
        subprocess.run([ADB_PATH, "wait-for-device"])

# Install the APK
        install_command = [ADB_PATH, "install", apk_path]
        subprocess.run(install_command)
        print(f"APK installed: {apk_path}")
    except Exception as e:
        print(f"Error: Failed to install APK. {str(e)}")


# Function to simulate a basic Android task
def launch_app(package_name):
    try:
# Launch the app using adb
        subprocess.run([ADB_PATH, "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"])
        print(f"App launched: {package_name}")
    except Exception as e:
        print(f"Error: Failed to launch app. {str(e)}")

def get_system_info():
    try:
# Get OS version
        os_version_result = subprocess.run([ADB_PATH, "shell", "getprop", "ro.build.version.release"], stdout=subprocess.PIPE)
        os_version = os_version_result.stdout.decode("utf-8").strip()
        
# Get device model
        model_result = subprocess.run([ADB_PATH, "shell", "getprop", "ro.product.model"], stdout=subprocess.PIPE)
        model = model_result.stdout.decode("utf-8").strip()
        
# Get available memory
        memory_result = subprocess.run([ADB_PATH, "shell", "cat", "/proc/meminfo"], stdout=subprocess.PIPE)
        memory_info = memory_result.stdout.decode("utf-8").strip()
        
# Parse available memory (in kB)
        available_memory_line = [line for line in memory_info.split('\n') if "MemAvailable" in line]
        if available_memory_line:
            available_memory = available_memory_line[0].split(":")[1].strip()
        else:
            available_memory = "Not available"
        
# Log the information
        print("System Information:")
        print(f"OS Version: {os_version}")
        print(f"Device Model: {model}")
        print(f"Available Memory: {available_memory} kB")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Create a basic CLI interface to control the virtual Android system
def create_cli():
    print("\nVirtual Android System")
    print("------------------------")
    
    while True:
        print("\nMenu:")
        print("1. Launch Emulator")
        print("2. Launch Apps")
        print("3. install app")
        print("4. get info")
        print("5. Exit")

        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            launch_android_emulator()
        elif choice == "2":
            print("\nInstalled Apps:")
            apps = {
                1: "com.android.chrome",  # Example package names for apps
                2: "com.android.calculator2",
                3: "com.android.gallery3d",
                4: "com.android.settings"
            }
            for i, app in apps.items():
                print(f"{i}. {app}")

            app_choice = input("\nEnter the number of the app to launch (1-4): ").strip()

            try:
                app_choice = int(app_choice)
                if 1 <= app_choice <= len(apps):
                    launch_app(apps[app_choice])  
                else:
                    print("Invalid app selection. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Exiting Virtual Android System. Goodbye!")
            break
        elif choice == "3":
            apk_path = "C:/Users/praneet_bawa/AndroidStudioProjects/Msaak/app/build/outputs/apk/debug/app-debug.apk"
            install_apk(apk_path)
        elif choice == "4":
            get_system_info()
        else:
            print("Invalid choice. Please try again.")

# Main Execution
if __name__ == "__main__":
    create_cli()

# first load emulator 
# then perform other operations
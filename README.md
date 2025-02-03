# Dockerizing a Simple Web Application

This guide walks through setting up a simple web application using Flask and MySQL in Docker containers, with and without Docker Compose.

---

## **📌 Steps to Set Up the Project**

### **1️⃣ Create a Project Directory**
```bash
mkdir docker_project
cd docker_project
```

### **2️⃣ Create the Application File**
Create `app.py` and define your Flask application.

### **3️⃣ Create a Dockerfile**
Create a `Dockerfile` and define how the Flask app should be built.
```bash
vim Dockerfile
```

### **4️⃣ Build the Docker Image**
Run the following command to build the image:
```bash
docker build -t web-app .
```

### **5️⃣ Create a Docker Network**
To enable communication between containers, create a custom bridge network:
```bash
docker network create -d bridge connector
```

### **6️⃣ Run the Containers**
#### **Run MySQL Container**
```bash
docker run -d --name mysql-container --network connector \
    -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=mysql \
    -p 3306:3306 mysql:8
```

#### **Run Flask Web Application**
```bash
docker run -d --name flask-container --network connector -p 5000:5000 web-app
```

### **7️⃣ Test the Application**
Open your browser and go to:
```
http://<your-public-ip>:5000
```
Or test the MySQL connection:
```
http://<your-public-ip>:5000/mysql
```

---

## **📌 Running with Docker Compose**
Instead of running multiple `docker run` commands, use `docker-compose`.

### **1️⃣ Create a Docker Compose File**
Create `docker-compose.yml`:
```bash
vim docker-compose.yml
```

### **2️⃣ Start the Services**
Run the following command:
```bash
docker-compose up -d
```

### **3️⃣ Verify the Application**
Check in the browser:
```
http://<your-public-ip>:5000

![Screenshot (27)](https://github.com/user-attachments/assets/0ad57b10-16ff-4523-9841-da1912405212)


http://<your-public-ip>:5000/mysql

![Screenshot (28)](https://github.com/user-attachments/assets/920b2507-7f3b-489a-9c8b-2db5376b4f67)


```

---

## **✅ Conclusion**
By following these steps, you've successfully:
- Dockerized a Flask application.
- Connected it with MySQL using a Docker network.
- Deployed the setup with and without Docker Compose.

Now your web application is fully containerized and can run anywhere with Docker! 🚀


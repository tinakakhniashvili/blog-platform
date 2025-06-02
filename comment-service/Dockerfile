# Use the official OpenJDK image for Java 17 (adjust if needed)
FROM openjdk:17-jdk-slim

# Set the working directory
WORKDIR /app

# Copy the JAR built by Maven into the container
COPY target/comment-service-0.0.1-SNAPSHOT.jar app.jar

# Run the JAR
ENTRYPOINT ["java", "-jar", "app.jar"]

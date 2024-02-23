# Inception

## Project Overview

### Components

- **NGINX**: Serves as the entrypoint via port 443, using TLSv1.2 or TLSv1.3 for secure communication.
  
- **WordPress + php-fpm**: Hosts the WordPress application. No nginx is included.

- **MariaDB**: Manages the project's database.

- **Volumes**: Two volumes are used - one for the WordPress database and another for website files.

- **Docker Network**: Ensures seamless communication between containers.

### Bonus Services

In addition to the core services, the project includes the following bonus services, each running in its own container:

- **Redis Cache**: Set up a Redis cache for your WordPress website to enhance cache management.

- **FTP Server**: A dedicated FTP server container points to the volume of your WordPress website for easy file management.

- **Static Website**: Create a simple static website in the language of your choice (excluding PHP), such as a showcase site or a resume presentation.

- **Adminer**: A service to manage your MariaDB database easily.

- **Grafana**: Set up Grafana, a powerful monitoring and visualization platform, for various use cases. Justification for this choice can be provided during the project defense.

## Configuration

- **Security**: No passwords are stored in Dockerfiles. Environment variables are used for configuration, and a `.env` file at the root of the `srcs` directory stores these variables.

- **Database**: MariaDB is configured with two users, including an administrator. The administrator's username avoids common "admin" patterns.

## Usage

1. Clone the project repository.

2. Create a `.env` file in the `srcs` directory to store environment variables. (A custom one is provided)

3. Build and start the project using the provided Makefile:

```bash
make    # Build and run custom Docker images
make <service>       # Execute 'sh' in the container <service> (E.g.: make mariadb executes sh in the mariadb container)
```

5. When done, stop and remove the containers:

```bash
make down     # Stop and remove containers
```

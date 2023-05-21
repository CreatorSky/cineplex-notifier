# Cineplex Notifier

Cineplex Notifier is a Python application that allows you to receive alerts when ticket booking starts for upcoming movies at Cineplex. By providing the movie URL and your phone number, it sends you notifications to keep you informed about the ticket availability.

## Features

- Receive timely alerts when ticket booking starts for your desired movie at Cineplex.
- Easily configurable through environment variables.
- Dockerized for easy deployment and usage.

## Prerequisites

Before running the Cineplex Notifier application, ensure that you have the following prerequisites installed:

- Make
- Docker

## Configuration

The Cineplex Notifier application requires the following environment variables to be set. You can set these variables in the `docker-compose.yml` file:

- `URL`: The URL of the upcoming movie at Cineplex. For example: `https://www.cineplex.com/movie/oppenheimer`.
- `EMAIL`: The Gmail email address to be used as the sender's email in the SMTP server.
- `PASSWORD`: The Gmail app password to send text messages via email from your email address to your phone. [MORE INFO](https://support.google.com/accounts/answer/185833)
- `PHONE`: The phone number(s) and provider(s) to receive the notifications. Multiple phone numbers and providers can be specified, separated by commas. For example: `PHONE#1:PROVIDER1,PHONE#2:PROVIDER2`.

## Usage

Follow the steps below to run the Cineplex Notifier application:

1. Update the environment variables in the `docker-compose.yml` file with your specific values.

2. Build the Docker image:

   ```
   make build
   ```

3. Run the application:
   ```
   make run
   ```
   The Cineplex Notifier will start monitoring the specified movie URL, and you will receive alerts when ticket booking starts. 

4. To stop the application:
   ```
   make stop
   ```
5. To purge the running container and remove it:
   ```
   make purge
   ```
## License

This project is licensed under the MIT License.

## Contact

For any questions, suggestions, or contributions, please feel free to contact us:

**Project Maintainer:** Akash Parmar \
**Email:** akashparmarsoftware@gmail.com \
**GitHub:** [CreatorSky](https://github.com/creatorsky)

We welcome any feedback and appreciate your interest in contributing to the project!

# NOT TO BE USED FOR REAL WORLD FLYING THIS IS STRICTLY ONLY FOR FLIGHT SIMULATION USAGE

# X-TensibleAPI
The Xtensible API is a powerful and user-friendly solution designed to enhance your X-Plane 11 flight simulation experience by enabling remote control of the aircraft using a phone or tablet. 

# Flight Checklist Application

![Image Description](https://i.imgur.com/dwAiXqm.gif)
## Features

- **Interactive Checklists:** Step-by-step checklists for various phases of flight.
- **Responsive Design:** Adapts to different screen sizes.
- **Navigation Bar:** Quick access to different checklist sections.
- **Button Interactions:** Each button performs a specific command related to the checklist item.
- **Visual Feedback:** Buttons change color when clicked to indicate completion.
- **Backend Communication:** Sends commands to X-Plane 11 using UDP.

## Technologies Used

### Frontend:

- **HTML5:** Markup language for structuring the content.
- **CSS3:** Styling the application, including custom styles for buttons and layout.
- **Bootstrap 4.5.2:** For responsive design and navigation bar components.
- **Swiper.js:** For creating swipeable slides to navigate through the checklist items.
- **JavaScript:** For handling button interactions and Swiper.js initialization.

### Backend:

- **FastAPI:** Framework for building the backend server.
- **Socket Programming:** For sending commands to X-Plane 11 via UDP.

## File Structure

### frontend:

- `index.html`: Main HTML file containing the structure of the web application.
- `styles.css`: Custom CSS styles defined within the `<style>` tag in the HTML.
- `swiper-bundle.min.css`: CSS file for Swiper.js library.
- `bootstrap.min.css`: CSS file for Bootstrap library.

### backend:

- `main.py`: FastAPI application handling HTTP requests and sending UDP commands to X-Plane 11.

## Code Overview

### Frontend

- **HTML Structure:**
  - Head Section: Includes meta tags, title, and links to external CSS files.
  - Body Section: Contains the navigation bar and Swiper container with multiple slides for each checklist phase.
- **CSS Styling:**
  - Body: Sets font, background color, and text color.
  - Swiper: Defines dimensions and styles for Swiper container and slides.
  - Buttons: Custom styles for command buttons, including hover effects and clicked state.
- **JavaScript:**
  - Swiper Initialization: Initializes Swiper with specific parameters for navigation.
  - Button Click Events: Handles the visual feedback when buttons are clicked.

### Backend

- **FastAPI Server:**
  - Static Files: Serves static files (HTML, CSS, JS).
  - Index Route: Serves the main HTML file.
  - Command Route: Receives commands from the frontend and sends them to X-Plane 11 via UDP.
- **Socket Communication:**
  - UDP Protocol: Sends commands to the local IP (127.0.0.1) on port 49000 using UDP.

## Usage

1. **Clone the Repository:** `git clone <repository-url>`
2. **Install Dependencies:** `pip install fastapi uvicorn`
3. **Run the Server:** `uvicorn main:app --reload`
4. **Open the Application:** Access the application on another device by navigating to `http://<server-ip>:8000` in a web browser.
5. **Navigate:** Use the navigation bar to access different checklist phases.
6. **Interact:** Click on buttons to perform checklist actions and see visual feedback.

## Contribution

Feel free to fork the repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

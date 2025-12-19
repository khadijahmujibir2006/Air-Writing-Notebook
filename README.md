🖐️ Air Writing Notebook using Computer Vision

A gesture-based air writing system that allows users to write in the air using hand movements captured via a webcam.
This project uses Computer Vision and Hand Gesture Recognition to provide a touch-free writing experience with advanced features like Undo, Redo, Color Selection, and Canvas Clearing.

📌 Features

✍️ Write in the air using your index finger

🎨 Change drawing colors using hand gestures

↩️ Undo last stroke using a fist gesture

↪️ Redo using open-hand gesture

🧹 Clear the canvas using two fingers

💾 Save handwritten notes as an image

🎥 Real-time hand tracking using webcam

🛠️ Technologies Used

Python 3.10

OpenCV – video capture & drawing

MediaPipe – hand landmark detection

NumPy – canvas operations

Pillow – image saving

VS Code – development environment

📂 Project Structure
Air-Writing-Notebook/
│
├── main.py              # Main application logic
├── hand_tracking.py     # Hand detection using MediaPipe
├── gestures.py          # Finger state detection
├── canvas.py            # Drawing, undo & redo logic
├── save_utils.py        # Save output as image
├── .gitignore
└── README.md

✋ Gesture Controls
Gesture	Action
☝ Index Finger	Draw
👍 Thumb	Red color
✌ Index + Middle	Green color / Clear canvas
🤟 Index + Pinky	Blue color
✊ Fist	Undo
✋ All fingers open	Redo / Pink color
Q key	Save & Exit
▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/khadijahmujibir2006/Air-Writing-Notebook.git
cd Air-Writing-Notebook

2️⃣ Create virtual environment
py -3.10 -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install opencv-python mediapipe==0.10.9 numpy pillow reportlab

4️⃣ Run the application
python main.py

🧠 How It Works

MediaPipe detects 21 hand landmarks in real time.

Finger positions are analyzed to identify gestures.

OpenCV is used to draw strokes on a virtual canvas.

Undo/Redo is implemented using stack-based state management.

Different finger combinations control colors and actions.

🎯 Use Cases

Touchless note-taking

Smart classrooms

Interactive presentations

Assistive technology

Computer vision learning project

📈 Future Enhancements

Save notes as PDF

Add text recognition

Multi-hand support

Gesture-based UI buttons

Streamlit web version

👩‍💻 Author

Khadijah Mujibir Rahman
B.E. Computer Science and Engineering
St. Joseph’s Institute of Technology

🔗 GitHub: https://github.com/khadijahmujibir2006

⭐ Acknowledgements

Google MediaPipe

OpenCV community

Python open-source ecosystem


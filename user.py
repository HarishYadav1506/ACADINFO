import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import random
import json
import os
import hashlib
from datetime import datetime, timedelta


class AcadInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ACADINFO - Enlightens Your Dream")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")

        # Load data
        self.load_data()

        # Current user state
        self.current_user = None
        self.user_data = {}

        # Style configuration
        self.configure_styles()

        # Create menu bar
        self.create_menu()

        # Main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Show login screen by default
        self.show_login_screen()

    def configure_styles(self):
        """Configure the visual styles for the application"""
        self.style = ttk.Style()

        # Frame styles
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('Card.TFrame', background='white', borderwidth=1, relief='solid')

        # Label styles
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'), foreground='#3498db')
        self.style.configure('Subtitle.TLabel', font=('Arial', 12), foreground='#7f8c8d')
        self.style.configure('Success.TLabel', foreground='#27ae60')
        self.style.configure('Error.TLabel', foreground='#e74c3c')

        # Button styles
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('Accent.TButton', background='#3498db', foreground='white')
        self.style.map('Accent.TButton', background=[('active', '#2980b9')])
        self.style.configure('Premium.TButton', background='#27ae60', foreground='white')
        self.style.map('Premium.TButton', background=[('active', '#219653')])
        self.style.configure('Danger.TButton', background='#e74c3c', foreground='white')
        self.style.map('Danger.TButton', background=[('active', '#c0392b')])

        # Entry styles
        self.style.configure('TEntry', padding=5)

        # Combobox styles
        self.style.configure('TCombobox', padding=5)

    def load_data(self):
        """Load all hardcoded data for the application"""
        # Sports data
        self.sports = ["Cricket", "Football", "Basketball", "Chess", "Hockey", "Tennis", "Badminton", "Table Tennis",
                       "Volleyball", "Swimming"]

        # States and cities data
        self.states = {
            "Delhi": ["New Delhi", "Noida", "Gurgaon", "Faridabad", "Ghaziabad"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
            "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore"],
            "West Bengal": ["Kolkata", "Howrah", "Durgapur"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
            "Telangana": ["Hyderabad", "Warangal", "Karimnagar"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
            "Punjab": ["Chandigarh", "Ludhiana", "Amritsar"]
        }

        # Academies data with detailed information
        self.academies = {
            "Cricket": {
                "Delhi": [
                    {"name": "Delhi Cricket Academy", "rating": 4.7, "coach": "Rahul Sharma", "established": 2005,
                     "facilities": ["3 grounds", "Indoor nets", "Gym", "Swimming pool"],
                     "address": "123 Sports Complex, New Delhi",
                     "contact": "011-23456789",
                     "fees": "₹15,000 per quarter",
                     "timings": "6:00 AM - 9:00 AM, 4:00 PM - 7:00 PM"},
                    {"name": "National Cricket Center", "rating": 4.9, "coach": "Vikram Rathore", "established": 1998,
                     "facilities": ["5 grounds", "Swimming pool", "Hostel", "Cafeteria", "Physiotherapy center"],
                     "address": "National Stadium Road, Delhi",
                     "contact": "011-34567890",
                     "fees": "₹25,000 per quarter",
                     "timings": "5:30 AM - 8:30 AM, 3:30 PM - 6:30 PM"}
                ],
                "Maharashtra": [
                    {"name": "Mumbai Cricket Club", "rating": 4.8, "coach": "Sanjay Bangar", "established": 2001,
                     "facilities": ["2 grounds", "Indoor nets", "Gym"],
                     "address": "Marine Drive, Mumbai",
                     "contact": "022-45678901",
                     "fees": "₹18,000 per quarter",
                     "timings": "6:00 AM - 9:00 AM, 4:00 PM - 7:00 PM"},
                    {"name": "Pune Sports Academy", "rating": 4.5, "coach": "Hrishikesh Kanitkar", "established": 2010,
                     "facilities": ["3 grounds", "Gym", "Swimming pool"],
                     "address": "University Road, Pune",
                     "contact": "020-56789012",
                     "fees": "₹12,000 per quarter",
                     "timings": "6:30 AM - 9:30 AM, 4:30 PM - 7:30 PM"}
                ],
                "Karnataka": [
                    {"name": "Bangalore Cricket Institute", "rating": 4.6, "coach": "Venkatesh Prasad",
                     "established": 2003,
                     "facilities": ["4 grounds", "Hostel", "Gym", "Cafeteria"],
                     "address": "MG Road, Bangalore",
                     "contact": "080-67890123",
                     "fees": "₹20,000 per quarter",
                     "timings": "6:00 AM - 9:00 AM, 4:00 PM - 7:00 PM"}
                ]
            },
            "Football": {
                "Delhi": [
                    {"name": "Delhi Football School", "rating": 4.3, "coach": "Clifford Miranda", "established": 2007,
                     "facilities": ["Full-size pitch", "Gym", "Changing rooms"],
                     "address": "Dwarka Sports Complex, Delhi",
                     "contact": "011-78901234",
                     "fees": "₹10,000 per quarter",
                     "timings": "5:00 AM - 8:00 AM, 3:00 PM - 6:00 PM"},
                    {"name": "Soccer Excellence", "rating": 4.4, "coach": "Bhaichung Bhutia", "established": 2012,
                     "facilities": ["2 pitches", "Hostel", "Gym", "Cafeteria"],
                     "address": "Greater Kailash, Delhi",
                     "contact": "011-89012345",
                     "fees": "₹15,000 per quarter",
                     "timings": "5:30 AM - 8:30 AM, 3:30 PM - 6:30 PM"}
                ],
                "Maharashtra": [
                    {"name": "Mumbai Football Academy", "rating": 4.5, "coach": "Derrick Pereira", "established": 2005,
                     "facilities": ["Full-size pitch", "Swimming pool", "Gym"],
                     "address": "Andheri Sports Complex, Mumbai",
                     "contact": "022-90123456",
                     "fees": "₹12,000 per quarter",
                     "timings": "5:00 AM - 8:00 AM, 4:00 PM - 7:00 PM"}
                ],
                "West Bengal": [
                    {"name": "Kolkata Football Club", "rating": 4.7, "coach": "Subrata Bhattacharya",
                     "established": 1995,
                     "facilities": ["3 pitches", "Hostel", "Gym", "Medical center"],
                     "address": "Salt Lake Stadium, Kolkata",
                     "contact": "033-01234567",
                     "fees": "₹8,000 per quarter",
                     "timings": "5:30 AM - 8:30 AM, 3:30 PM - 6:30 PM"}
                ]
            },
            "Basketball": {
                "Delhi": [
                    {"name": "Delhi Basketball Academy", "rating": 4.2, "coach": "Ajmer Singh", "established": 2008,
                     "facilities": ["3 courts", "Gym", "Changing rooms"],
                     "address": "Thyagaraj Stadium, Delhi",
                     "contact": "011-12345678",
                     "fees": "₹9,000 per quarter",
                     "timings": "6:00 AM - 9:00 AM, 4:00 PM - 7:00 PM"}
                ],
                "Karnataka": [
                    {"name": "Bangalore Basketball Center", "rating": 4.4, "coach": "Prashanti Singh",
                     "established": 2011,
                     "facilities": ["4 courts", "Gym", "Hostel"],
                     "address": "Koramangala, Bangalore",
                     "contact": "080-23456789",
                     "fees": "₹11,000 per quarter",
                     "timings": "6:30 AM - 9:30 AM, 4:30 PM - 7:30 PM"}
                ]
            },
            "Chess": {
                "Delhi": [
                    {"name": "Delhi Chess Club", "rating": 4.8, "coach": "RB Ramesh", "established": 2000,
                     "facilities": ["Air-conditioned halls", "Library", "Analysis rooms"],
                     "address": "Connaught Place, Delhi",
                     "contact": "011-34567890",
                     "fees": "₹6,000 per quarter",
                     "timings": "9:00 AM - 9:00 PM"}
                ],
                "Tamil Nadu": [
                    {"name": "Chennai Chess Academy", "rating": 4.7, "coach": "Viswanathan Anand", "established": 2005,
                     "facilities": ["Air-conditioned halls", "Digital analysis boards", "Library"],
                     "address": "Nungambakkam, Chennai",
                     "contact": "044-45678901",
                     "fees": "₹7,500 per quarter",
                     "timings": "10:00 AM - 8:00 PM"}
                ]
            },
            "Hockey": {
                "Delhi": [
                    {"name": "Delhi Hockey Academy", "rating": 4.5, "coach": "Dhanraj Pillay", "established": 2003,
                     "facilities": ["2 astroturf pitches", "Gym", "Hostel"],
                     "address": "National Stadium, Delhi",
                     "contact": "011-56789012",
                     "fees": "₹12,000 per quarter",
                     "timings": "5:30 AM - 8:30 AM, 4:30 PM - 7:30 PM"}
                ],
                "Maharashtra": [
                    {"name": "Mumbai Hockey Club", "rating": 4.3, "coach": "Viren Rasquinha", "established": 2007,
                     "facilities": ["Astroturf pitch", "Gym", "Changing rooms"],
                     "address": "Mahalaxmi, Mumbai",
                     "contact": "022-67890123",
                     "fees": "₹10,000 per quarter",
                     "timings": "6:00 AM - 9:00 AM, 4:00 PM - 7:00 PM"}
                ]
            }
        }

        # Courses data with detailed information
        self.courses = {
            1: {
                "id": 1,
                "title": "Fundamentals of Sports Training",
                "price": 799,
                "duration": "4 weeks",
                "instructor": "Professional Coach",
                "sport": "General",
                "description": "Learn the basic principles of sports training, nutrition, and injury prevention. This course is perfect for beginners who want to understand the fundamentals of athletic training.",
                "modules": ["Introduction to Sports Science", "Basic Training Principles", "Nutrition Basics",
                            "Injury Prevention", "Recovery Techniques"],
                "image": "course1.jpg",
                "students": 1245,
                "rating": 4.5
            },
            2: {
                "id": 2,
                "title": "Advanced Cricket Techniques",
                "price": 1299,
                "duration": "8 weeks",
                "instructor": "International Player",
                "sport": "Cricket",
                "description": "Master advanced batting, bowling and fielding techniques with professional guidance from former international players. Includes video analysis of your technique.",
                "modules": ["Advanced Batting", "Fast Bowling Techniques", "Spin Bowling Variations", "Fielding Drills",
                            "Match Situations", "Mental Toughness"],
                "image": "course2.jpg",
                "students": 876,
                "rating": 4.7
            },
            3: {
                "id": 3,
                "title": "Football Strategy Masterclass",
                "price": 999,
                "duration": "6 weeks",
                "instructor": "Pro Football Coach",
                "sport": "Football",
                "description": "Learn advanced tactics and strategies from professional football coaches. Includes video analysis of professional matches.",
                "modules": ["Formations and Systems", "Set Piece Strategies", "Pressing Techniques", "Counter Attacks",
                            "Defensive Organization"],
                "image": "course3.jpg",
                "students": 654,
                "rating": 4.6
            },
            4: {
                "id": 4,
                "title": "Basketball Skills Development",
                "price": 899,
                "duration": "5 weeks",
                "instructor": "NBA Trainer",
                "sport": "Basketball",
                "description": "Develop your basketball skills with training methods used by professional players. Includes personalized feedback on your game.",
                "modules": ["Shooting Techniques", "Ball Handling", "Defensive Moves", "Rebounding", "Game IQ"],
                "image": "course4.jpg",
                "students": 432,
                "rating": 4.4
            },
            5: {
                "id": 5,
                "title": "Chess Grandmaster Training",
                "price": 1499,
                "duration": "10 weeks",
                "instructor": "Grandmaster",
                "sport": "Chess",
                "description": "Learn advanced chess strategies from a grandmaster. Includes analysis of your games and personalized training plan.",
                "modules": ["Opening Repertoire", "Middle Game Strategies", "Endgame Techniques", "Tactical Patterns",
                            "Time Management"],
                "image": "course5.jpg",
                "students": 765,
                "rating": 4.8
            }
        }

        # Webinars data
        self.webinars = {
            1: {
                "id": 1,
                "title": "Sports Nutrition for Peak Performance",
                "price": 399,
                "date": "Wednesday, 15th March 2023",
                "time": "6:00 PM - 7:00 PM",
                "duration": "1 hour",
                "instructor": "Dr. Anjali Sharma (Sports Dietician)",
                "description": "Learn about optimal nutrition for athletes and how to fuel your performance. Includes Q&A session with the dietician.",
                "image": "webinar1.jpg",
                "seats": 100,
                "registered": 78
            },
            2: {
                "id": 2,
                "title": "Mental Toughness in Sports",
                "price": 349,
                "date": "Friday, 17th March 2023",
                "time": "7:00 PM - 8:00 PM",
                "duration": "1 hour",
                "instructor": "Sports Psychologist",
                "description": "Develop mental resilience and learn techniques to handle pressure in competitive situations.",
                "image": "webinar2.jpg",
                "seats": 100,
                "registered": 65
            },
            3: {
                "id": 3,
                "title": "Injury Prevention and Recovery",
                "price": 349,
                "date": "Saturday, 18th March 2023",
                "time": "5:00 PM - 6:00 PM",
                "duration": "1 hour",
                "instructor": "Physiotherapist",
                "description": "Learn how to prevent common sports injuries and proper recovery techniques.",
                "image": "webinar3.jpg",
                "seats": 100,
                "registered": 53
            },
            4: {
                "id": 4,
                "title": "Strength and Conditioning for Athletes",
                "price": 449,
                "date": "Tuesday, 21st March 2023",
                "time": "6:30 PM - 7:30 PM",
                "duration": "1 hour",
                "instructor": "Strength Coach",
                "description": "Learn proper strength training techniques tailored for your sport.",
                "image": "webinar4.jpg",
                "seats": 100,
                "registered": 42
            }
        }

        # Equipment store items
        self.equipment = {
            1: {
                "id": 1,
                "name": "Cricket Bat (MRF Genius Grand Edition)",
                "price": 3499,
                "category": "Cricket",
                "discount": 15,
                "description": "Premium English willow cricket bat with perfect weight balance",
                "image": "bat1.jpg",
                "stock": 25,
                "rating": 4.7
            },
            2: {
                "id": 2,
                "name": "Football (Nike Premier League)",
                "price": 1999,
                "category": "Football",
                "discount": 10,
                "description": "Official match ball with high-performance texture",
                "image": "football1.jpg",
                "stock": 40,
                "rating": 4.5
            },
            3: {
                "id": 3,
                "name": "Basketball (Spalding NBA Official)",
                "price": 2499,
                "category": "Basketball",
                "discount": 12,
                "description": "Official NBA game ball with premium composite leather",
                "image": "basketball1.jpg",
                "stock": 30,
                "rating": 4.6
            },
            4: {
                "id": 4,
                "name": "Chess Set (Staunton Tournament)",
                "price": 1299,
                "category": "Chess",
                "discount": 5,
                "description": "Professional tournament chess set with 3.75\" king",
                "image": "chess1.jpg",
                "stock": 50,
                "rating": 4.8
            },
            5: {
                "id": 5,
                "name": "Hockey Stick (Adidas X Series)",
                "price": 2799,
                "category": "Hockey",
                "discount": 8,
                "description": "Carbon fiber hockey stick with optimal bow for power and control",
                "image": "hockey1.jpg",
                "stock": 20,
                "rating": 4.4
            }
        }

        # News and articles
        self.articles = [
            {
                "title": "How to Choose the Right Sports Academy for Your Child",
                "date": "March 10, 2023",
                "author": "Sports Education Expert",
                "summary": "A comprehensive guide to selecting the best sports academy based on your child's interests and goals.",
                "image": "article1.jpg"
            },
            {
                "title": "The Importance of Mental Training in Sports",
                "date": "March 5, 2023",
                "author": "Sports Psychologist",
                "summary": "Exploring how mental conditioning can improve athletic performance as much as physical training.",
                "image": "article2.jpg"
            },
            {
                "title": "Balancing Academics and Sports: A Parent's Guide",
                "date": "February 28, 2023",
                "author": "Education Counselor",
                "summary": "Tips for helping young athletes maintain academic excellence while pursuing sports.",
                "image": "article3.jpg"
            }
        ]

        # Testimonials
        self.testimonials = [
            {
                "name": "Rahul Sharma",
                "role": "Cricket Player",
                "text": "ACADINFO helped me find the perfect academy to take my cricket to the next level. The coaches are excellent!",
                "image": "testimonial1.jpg"
            },
            {
                "name": "Priya Patel",
                "role": "Parent",
                "text": "As a parent, I was confused about which academy to choose for my daughter. ACADINFO made the process so easy!",
                "image": "testimonial2.jpg"
            },
            {
                "name": "Coach Arjun",
                "role": "Football Coach",
                "text": "Our academy has seen a 40% increase in registrations since joining ACADINFO. Great platform!",
                "image": "testimonial3.jpg"
            }
        ]

        # Load users from file or create default
        self.users_file = "users.json"
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            # Default admin account
            self.users = {
                "admin": {
                    "password": self.hash_password("admin123"),
                    "email": "admin@acadinfo.com",
                    "full_name": "Administrator",
                    "phone": "9162960922",
                    "premium": True,
                    "joined": datetime.now().strftime("%Y-%m-%d"),
                    "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "bookings": []
                }
            }
            self.save_users()

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def save_users(self):
        """Save users to file"""
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=2)

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="My Profile", command=self.show_profile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_dialog)
        help_menu.add_command(label="Contact Support", command=self.show_contact_dialog)
        help_menu.add_command(label="User Guide", command=self.show_user_guide)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def clear_main_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_main_container()
        self.current_user = None

        # Container for centering
        center_frame = ttk.Frame(self.main_container)
        center_frame.pack(expand=True, fill=tk.BOTH, padx=100, pady=50)

        # Login card
        login_card = ttk.Frame(center_frame, style='Card.TFrame', padding=30)
        login_card.pack(expand=True, fill=tk.BOTH)

        # Logo
        logo_frame = ttk.Frame(login_card)
        logo_frame.pack(pady=(0, 20))

        # Placeholder for logo image
        logo_placeholder = tk.Label(logo_frame, text="⚽", font=('Arial', 48))
        logo_placeholder.pack(side=tk.LEFT, padx=10)

        logo_text_frame = ttk.Frame(logo_frame)
        logo_text_frame.pack(side=tk.LEFT)

        ttk.Label(logo_text_frame, text="ACADINFO", style='Title.TLabel').pack(anchor=tk.W)
        ttk.Label(logo_text_frame, text="Enlightens Your Dream", style='Subtitle.TLabel').pack(anchor=tk.W)

        # Login form
        form_frame = ttk.Frame(login_card)
        form_frame.pack(fill=tk.X, pady=10)

        ttk.Label(form_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.username_entry = ttk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        ttk.Label(form_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.password_entry = ttk.Entry(form_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)

        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        ttk.Checkbutton(form_frame, text="Remember me", variable=self.remember_var).grid(row=2, column=1, sticky=tk.W,
                                                                                         pady=5)

        buttons_frame = ttk.Frame(login_card)
        buttons_frame.pack(fill=tk.X, pady=20)

        login_btn = ttk.Button(buttons_frame, text="Login", style='Accent.TButton', command=self.authenticate)
        login_btn.pack(side=tk.LEFT, padx=10)

        register_btn = ttk.Button(buttons_frame, text="Register", command=self.show_register_dialog)
        register_btn.pack(side=tk.LEFT, padx=10)

        forgot_btn = ttk.Button(buttons_frame, text="Forgot Password?", command=self.show_forgot_password_dialog)
        forgot_btn.pack(side=tk.RIGHT, padx=10)

        # Focus on username field
        self.username_entry.focus_set()

        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.authenticate())

    def authenticate(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        if username in self.users:
            hashed_password = self.hash_password(password)
            if self.users[username]["password"] == hashed_password:
                self.current_user = username
                self.user_data = self.users[username]

                # Update last login
                self.users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_users()

                self.show_main_app()
            else:
                messagebox.showerror("Login Failed", "Invalid password")
        else:
            messagebox.showerror("Login Failed", "Username not found")

    def show_register_dialog(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register New Account")
        register_window.geometry("400x500")
        register_window.resizable(False, False)

        # Form frame
        form_frame = ttk.Frame(register_window, padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(form_frame, text="Create New Account", style='Header.TLabel').pack(pady=10)

        # Form fields
        fields = [
            ("Username:", "username"),
            ("Email:", "email"),
            ("Password:", "password", True),
            ("Confirm Password:", "confirm_password", True),
            ("Full Name:", "full_name"),
            ("Phone:", "phone")
        ]

        self.register_entries = {}

        for i, field in enumerate(fields):
            label_text, field_name, *is_password = field
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky=tk.E)

            if is_password:
                entry = ttk.Entry(form_frame, show="*")
            else:
                entry = ttk.Entry(form_frame)

            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)
            self.register_entries[field_name] = entry

        # User type selection
        ttk.Label(form_frame, text="Registering as:").grid(row=len(fields), column=0, padx=5, pady=5, sticky=tk.E)
        self.user_type = tk.StringVar(value="student")

        student_radio = ttk.Radiobutton(form_frame, text="Student", variable=self.user_type, value="student")
        student_radio.grid(row=len(fields), column=1, sticky=tk.W)

        parent_radio = ttk.Radiobutton(form_frame, text="Parent", variable=self.user_type, value="parent")
        parent_radio.grid(row=len(fields) + 1, column=1, sticky=tk.W)

        # Terms checkbox
        self.terms_var = tk.BooleanVar()
        ttk.Checkbutton(form_frame, text="I agree to the Terms and Conditions",
                        variable=self.terms_var).grid(row=len(fields) + 2, columnspan=2, pady=10)

        # Register button
        register_btn = ttk.Button(form_frame, text="Register", style='Accent.TButton',
                                  command=lambda: self.register_user(register_window))
        register_btn.grid(row=len(fields) + 3, columnspan=2, pady=10)

    def register_user(self, window):
        username = self.register_entries["username"].get().strip()
        email = self.register_entries["email"].get().strip()
        password = self.register_entries["password"].get()
        confirm_password = self.register_entries["confirm_password"].get()
        full_name = self.register_entries["full_name"].get().strip()
        phone = self.register_entries["phone"].get().strip()
        user_type = self.user_type.get()

        # Validation
        if not all([username, email, password, confirm_password]):
            messagebox.showerror("Error", "Please fill all required fields")
            return

        if not self.terms_var.get():
            messagebox.showerror("Error", "You must agree to the Terms and Conditions")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters")
            return

        if not any(char.isdigit() for char in password):
            messagebox.showerror("Error", "Password must contain at least one number")
            return

        if not any(char.isupper() for char in password):
            messagebox.showerror("Error", "Password must contain at least one uppercase letter")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists")
            return

        # Check if email is already registered
        for user in self.users.values():
            if user.get("email") == email:
                messagebox.showerror("Error", "Email already registered")
                return

        # Create new user
        self.users[username] = {
            "password": self.hash_password(password),
            "email": email,
            "full_name": full_name,
            "phone": phone,
            "type": user_type,
            "premium": False,
            "joined": datetime.now().strftime("%Y-%m-%d"),
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bookings": []
        }

        self.save_users()

        messagebox.showinfo("Success", "Registration successful! You can now login.")
        window.destroy()

    def show_forgot_password_dialog(self):
        forgot_window = tk.Toplevel(self.root)
        forgot_window.title("Password Recovery")
        forgot_window.geometry("400x250")
        forgot_window.resizable(False, False)

        # Form frame
        form_frame = ttk.Frame(forgot_window, padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(form_frame, text="Password Recovery", style='Header.TLabel').pack(pady=10)
        ttk.Label(form_frame, text="Enter your email address:").pack(pady=5)

        email_entry = ttk.Entry(form_frame)
        email_entry.pack(pady=5, fill=tk.X)

        def send_recovery():
            email = email_entry.get().strip()
            if not email:
                messagebox.showerror("Error", "Please enter your email address")
                return

            # Find user with this email
            found_user = None
            for username, data in self.users.items():
                if data.get("email") == email:
                    found_user = username
                    break

            if found_user:
                # In a real app, you would send an email with a reset link
                messagebox.showinfo("Success",
                                    f"Password reset instructions have been sent to {email}\n\n"
                                    "Please check your email to reset your password.")
                forgot_window.destroy()
            else:
                messagebox.showerror("Error", "No account found with this email address")

        send_btn = ttk.Button(form_frame, text="Send Recovery Email", style='Accent.TButton',
                              command=send_recovery)
        send_btn.pack(pady=10)

    def show_main_app(self):
        self.clear_main_container()

        # Header Frame
        header_frame = ttk.Frame(self.main_container, style='Card.TFrame')
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Logo and Title
        logo_frame = ttk.Frame(header_frame)
        logo_frame.pack(side=tk.LEFT, padx=10)

        logo_placeholder = tk.Label(logo_frame, text="⚽", font=('Arial', 24))
        logo_placeholder.pack(side=tk.LEFT)

        logo_text_frame = ttk.Frame(logo_frame)
        logo_text_frame.pack(side=tk.LEFT, padx=5)

        ttk.Label(logo_text_frame, text="ACADINFO", style='Title.TLabel').pack(anchor=tk.W)
        ttk.Label(logo_text_frame, text="Enlightens Your Dream", style='Subtitle.TLabel').pack(anchor=tk.W)

        # User info
        user_frame = ttk.Frame(header_frame)
        user_frame.pack(side=tk.RIGHT, padx=10)

        ttk.Label(user_frame, text=f"Welcome, {self.user_data.get('full_name', self.current_user)}",
                  font=('Arial', 10, 'bold')).pack(anchor=tk.E)

        if self.user_data.get("premium", False):
            ttk.Label(user_frame, text="Premium Member", style='Success.TLabel').pack(anchor=tk.E)
        else:
            ttk.Label(user_frame, text="Standard Member").pack(anchor=tk.E)

        logout_btn = ttk.Button(user_frame, text="Logout", command=self.show_login_screen)
        logout_btn.pack(anchor=tk.E, pady=5)

        # Navigation Bar
        nav_frame = ttk.Frame(self.main_container)
        nav_frame.pack(fill=tk.X, padx=10, pady=5)

        buttons = [
            ("🏠 Home", self.show_home_page),
            ("🔍 Find Academies", self.show_find_academies_page),
            ("📚 Courses", self.show_courses_page),
            ("🎤 Webinars", self.show_webinars_page),
            ("🛒 Equipment", self.show_equipment_page),
            ("⭐ Upgrade", self.show_upgrade_page)
        ]

        for btn_text, cmd in buttons:
            btn = ttk.Button(nav_frame, text=btn_text, command=cmd)
            btn.pack(side=tk.LEFT, padx=5)

        # Main Content Frame
        self.content_frame = ttk.Frame(self.main_container)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Show home page by default
        self.show_home_page()

    def show_home_page(self):
        self.clear_content_frame()

        # Welcome Section
        welcome_frame = ttk.Frame(self.content_frame, style='Card.TFrame', padding=20)
        welcome_frame.pack(fill=tk.X, pady=10)

        welcome_label = ttk.Label(welcome_frame,
                                  text="Welcome to ACADINFO\n\n"
                                       "A platform for all the sports aspirants of the world who strive to be the best "
                                       "and represent their country at the international level. ACADINFO provides you "
                                       "the opportunity to pursue a career in sports even from the most remote places "
                                       "of the world.",
                                  font=('Arial', 12), justify=tk.CENTER)
        welcome_label.pack()

        # Quick Actions
        actions_frame = ttk.Frame(self.content_frame)
        actions_frame.pack(fill=tk.X, pady=10)

        actions = [
            ("🔍 Find Academies", self.show_find_academies_page),
            ("📚 Browse Courses", self.show_courses_page),
            ("🎤 View Webinars", self.show_webinars_page),
            ("🛒 Equipment Store", self.show_equipment_page)
        ]

        for i, (text, cmd) in enumerate(actions):
            frame = ttk.Frame(actions_frame, style='Card.TFrame', padding=10)
            frame.grid(row=0, column=i, padx=5, sticky=tk.NSEW)

            ttk.Label(frame, text=text, font=('Arial', 10)).pack(pady=5)
            ttk.Button(frame, text="Go", style='Accent.TButton', command=cmd).pack()

            actions_frame.columnconfigure(i, weight=1)

        # Target Sports Section
        sports_frame = ttk.LabelFrame(self.content_frame, text="Popular Sports", padding=10)
        sports_frame.pack(fill=tk.X, pady=10)

        sports_to_show = random.sample(self.sports, 5)  # Show 5 random sports

        for sport in sports_to_show:
            sport_btn = ttk.Button(sports_frame, text=sport, style='Accent.TButton',
                                   command=lambda s=sport: self.show_sport_academies(s))
            sport_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Features Section
        features_frame = ttk.LabelFrame(self.content_frame, text="Why Choose ACADINFO?", padding=10)
        features_frame.pack(fill=tk.X, pady=10)

        features = [
            "🏟️ 3D View of Academies - Virtual tours before you visit",
            "⭐ Ratings and Reviews - From real students and parents",
            "🏆 Achievement Records - Track records of academy alumni",
            "📝 Multiple Academy Registration - One platform for all applications",
            "💻 Online Courses and Webinars - Learn from anywhere",
            "🛒 Equipment Store - Quality gear with member discounts",
            "📱 Mobile Friendly - Access on any device"
        ]

        for feature in features:
            ttk.Label(features_frame, text=feature).pack(anchor=tk.W, pady=2)

        # Testimonials Section
        testimonials_frame = ttk.LabelFrame(self.content_frame, text="What Our Users Say", padding=10)
        testimonials_frame.pack(fill=tk.X, pady=10)

        testimonials_to_show = random.sample(self.testimonials, 2)  # Show 2 random testimonials

        for testimonial in testimonials_to_show:
            card = ttk.Frame(testimonials_frame, style='Card.TFrame', padding=10)
            card.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

            ttk.Label(card, text=f"\"{testimonial['text']}\"", font=('Arial', 10, 'italic'), wraplength=300).pack()
            ttk.Label(card, text=f"- {testimonial['name']}, {testimonial['role']}",
                      font=('Arial', 9, 'bold')).pack(anchor=tk.E, pady=(5, 0))

    def show_find_academies_page(self):
        self.clear_content_frame()

        ttk.Label(self.content_frame, text="Find Sports Academies", style='Header.TLabel').pack(pady=10)

        # Search Form
        form_frame = ttk.Frame(self.content_frame, style='Card.TFrame', padding=15)
        form_frame.pack(pady=10, fill=tk.X)

        # State Selection
        ttk.Label(form_frame, text="Select State:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.state_var = tk.StringVar()
        state_dropdown = ttk.Combobox(form_frame, textvariable=self.state_var, values=list(self.states.keys()))
        state_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        state_dropdown.set("Select state")

        # City Selection
        ttk.Label(form_frame, text="Select City:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.city_var = tk.StringVar()
        self.city_dropdown = ttk.Combobox(form_frame, textvariable=self.city_var, state='disabled')
        self.city_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # Sport Selection
        ttk.Label(form_frame, text="Select Sport:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.sport_var = tk.StringVar()
        sport_dropdown = ttk.Combobox(form_frame, textvariable=self.sport_var, values=self.sports)
        sport_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        sport_dropdown.set("Select sport")

        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)

        # Bind state selection to update cities
        state_dropdown.bind("<<ComboboxSelected>>", self.update_cities)

        # Search Button
        search_btn = ttk.Button(self.content_frame, text="Search Academies",
                                style='Accent.TButton', command=self.search_academies)
        search_btn.pack(pady=10)

        # Results Frame
        self.results_frame = ttk.Frame(self.content_frame)
        self.results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    def update_cities(self, event):
        state = self.state_var.get()
        if state in self.states:
            self.city_dropdown['values'] = self.states[state]
            self.city_dropdown['state'] = 'readonly'
            self.city_dropdown.set("Select city")
        else:
            self.city_dropdown['values'] = []
            self.city_dropdown['state'] = 'disabled'

    def search_academies(self):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        state = self.state_var.get()
        city = self.city_var.get()
        sport = self.sport_var.get()

        if state == "Select state" or city == "Select city" or sport == "Select sport":
            messagebox.showerror("Error", "Please select state, city and sport")
            return

        # Find academies (in a real app this would query a database)
        academies = []
        if sport in self.academies and state in self.academies[sport]:
            academies = self.academies[sport][state]

        if not academies:
            no_results_frame = ttk.Frame(self.results_frame, style='Card.TFrame', padding=20)
            no_results_frame.pack(fill=tk.BOTH, expand=True, pady=20)

            ttk.Label(no_results_frame, text=f"No academies found for {sport} in {city}, {state}",
                      font=('Arial', 12)).pack()

            suggest_label = ttk.Label(no_results_frame,
                                      text="We can notify you when academies become available in this area.",
                                      font=('Arial', 10))
            suggest_label.pack(pady=10)

            notify_btn = ttk.Button(no_results_frame, text="Notify Me", style='Accent.TButton',
                                    command=lambda: self.request_notification(sport, city, state))
            notify_btn.pack()
            return

        results_label = ttk.Label(self.results_frame,
                                  text=f"Found {len(academies)} academies for {sport} in {city}, {state}:",
                                  font=('Arial', 12, 'bold'))
        results_label.pack(pady=10, anchor=tk.W)

        for academy in academies:
            academy_frame = ttk.Frame(self.results_frame, style='Card.TFrame', padding=10)
            academy_frame.pack(fill=tk.X, pady=5)

            # Academy info
            info_frame = ttk.Frame(academy_frame)
            info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

            ttk.Label(info_frame, text=academy["name"], font=('Arial', 12, 'bold')).pack(anchor=tk.W)
            ttk.Label(info_frame, text=f"Coach: {academy['coach']} | Established: {academy['established']}").pack(
                anchor=tk.W)
            ttk.Label(info_frame, text=f"Facilities: {', '.join(academy['facilities'])}", wraplength=400).pack(
                anchor=tk.W)

            # Rating and actions
            action_frame = ttk.Frame(academy_frame)
            action_frame.pack(side=tk.RIGHT)

            # Rating (random for demo)
            rating_frame = ttk.Frame(action_frame)
            rating_frame.pack(pady=5)

            ttk.Label(rating_frame, text=f"⭐ {academy['rating']}/5.0").pack(side=tk.LEFT)

            # Buttons
            btn_frame = ttk.Frame(action_frame)
            btn_frame.pack()

            view_btn = ttk.Button(btn_frame, text="View Details",
                                  command=lambda a=academy: self.view_academy_details(a))
            view_btn.pack(side=tk.LEFT, padx=5)

            register_btn = ttk.Button(btn_frame, text="Register", style='Accent.TButton',
                                      command=lambda a=academy: self.register_for_academy(a))
            register_btn.pack(side=tk.LEFT, padx=5)

    def request_notification(self, sport, city, state):
        messagebox.showinfo("Notification Request",
                            f"We will notify you when {sport} academies become available in {city}, {state}.\n\n"
                            "Thank you for your interest!")

    def view_academy_details(self, academy):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Academy Details - {academy['name']}")
        details_window.geometry("700x600")

        # Main container
        container = ttk.Frame(details_window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text=academy["name"], font=('Arial', 16, 'bold')).pack(anchor=tk.W)
        ttk.Label(header_frame, text=f"⭐ {academy['rating']}/5.0 | {academy['established']} | {academy['coach']}").pack(
            anchor=tk.W)

        # Details frame
        details_frame = ttk.Frame(container)
        details_frame.pack(fill=tk.BOTH, expand=True)

        # Left column - info
        info_frame = ttk.Frame(details_frame)
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        details = [
            ("Address:", academy["address"]),
            ("Contact:", academy["contact"]),
            ("Fees:", academy["fees"]),
            ("Timings:", academy["timings"]),
            ("Facilities:", '\n'.join(f"• {facility}" for facility in academy["facilities"]))
        ]

        for i, (label, value) in enumerate(details):
            ttk.Label(info_frame, text=label, font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky=tk.NE, padx=5,
                                                                               pady=2)
            ttk.Label(info_frame, text=value, wraplength=300).grid(row=i, column=1, sticky=tk.NW, pady=2)

        info_frame.columnconfigure(1, weight=1)

        # Right column - actions
        action_frame = ttk.Frame(details_frame)
        action_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

        # 3D View button (simulated)
        if self.user_data.get("premium", False):
            view_3d_btn = ttk.Button(action_frame, text="View 3D Tour", style='Premium.TButton',
                                     command=lambda: messagebox.showinfo("3D View", "Launching 3D tour..."))
            view_3d_btn.pack(fill=tk.X, pady=5)
        else:
            ttk.Label(action_frame,
                      text="Upgrade to Premium for 3D Academy View",
                      foreground="blue", wraplength=150).pack(pady=5)

        # Register button
        register_btn = ttk.Button(action_frame, text="Register Now", style='Accent.TButton',
                                  command=lambda: self.register_for_academy(academy))
        register_btn.pack(fill=tk.X, pady=5)

        # Contact button
        contact_btn = ttk.Button(action_frame, text="Contact Academy",
                                 command=lambda: self.contact_academy(academy))
        contact_btn.pack(fill=tk.X, pady=5)

        # Reviews section
        reviews_frame = ttk.LabelFrame(container, text="Reviews", padding=10)
        reviews_frame.pack(fill=tk.X, pady=10)

        # Sample reviews
        reviews = [
            {"name": "Rahul P.", "rating": 4,
             "text": "Great facilities and coaching staff. My game has improved significantly."},
            {"name": "Priya M.", "rating": 5,
             "text": "Excellent academy with professional approach. Highly recommended."}
        ]

        for review in reviews:
            review_card = ttk.Frame(reviews_frame, style='Card.TFrame', padding=10)
            review_card.pack(fill=tk.X, pady=5)

            ttk.Label(review_card, text=f"{review['name']} - ⭐ {review['rating']}/5",
                      font=('Arial', 10, 'bold')).pack(anchor=tk.W)
            ttk.Label(review_card, text=review["text"], wraplength=500).pack(anchor=tk.W)

        # Add review button
        add_review_btn = ttk.Button(reviews_frame, text="Add Your Review", style='Accent.TButton',
                                    command=lambda: self.add_review(academy))
        add_review_btn.pack(pady=5)

    def contact_academy(self, academy):
        messagebox.showinfo("Contact Academy",
                            f"You can contact {academy['name']} at:\n\n"
                            f"Phone: {academy['contact']}\n"
                            f"Address: {academy['address']}\n\n"
                            "We recommend calling during their working hours.")

    def add_review(self, academy):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to add a review")
            return

        review_window = tk.Toplevel(self.root)
        review_window.title(f"Add Review for {academy['name']}")
        review_window.geometry("400x300")

        # Form frame
        form_frame = ttk.Frame(review_window, padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(form_frame, text="Your Rating:").pack(anchor=tk.W, pady=5)

        self.review_rating = tk.IntVar(value=5)
        rating_frame = ttk.Frame(form_frame)
        rating_frame.pack(anchor=tk.W)

        for i in range(1, 6):
            ttk.Radiobutton(rating_frame, text=str(i), variable=self.review_rating, value=i).pack(side=tk.LEFT)

        ttk.Label(form_frame, text="Your Review:").pack(anchor=tk.W, pady=5)

        self.review_text = tk.Text(form_frame, height=8, width=40)
        self.review_text.pack(fill=tk.X)

        def submit_review():
            review = self.review_text.get("1.0", tk.END).strip()
            if not review:
                messagebox.showerror("Error", "Please write your review")
                return

            messagebox.showinfo("Thank You", "Your review has been submitted!")
            review_window.destroy()

        submit_btn = ttk.Button(form_frame, text="Submit Review", style='Accent.TButton',
                                command=submit_review)
        submit_btn.pack(pady=10)

    def register_for_academy(self, academy):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to register for an academy")
            return

        response = messagebox.askyesno("Registration",
                                       f"Register for {academy['name']}?\n\n"
                                       f"Fees: {academy['fees']}\n\n"
                                       "You will receive contact information to complete your registration.")
        if response:
            # Add to user's bookings
            booking = {
                "type": "academy",
                "name": academy["name"],
                "sport": next((sport for sport, academies in self.academies.items()
                               if academy in academies.get(self.state_var.get(), [])), "Unknown"),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "status": "Pending"
            }

            self.users[self.current_user]["bookings"].append(booking)
            self.save_users()

            messagebox.showinfo("Success",
                                f"Registration request sent for {academy['name']}!\n\n"
                                "The academy will contact you shortly with further details.")

    def show_courses_page(self):
        self.clear_content_frame()

        ttk.Label(self.content_frame, text="Available Courses", style='Header.TLabel').pack(pady=10)

        # Filter for premium users
        show_all = self.user_data.get("premium", False)

        # Search and filter frame
        filter_frame = ttk.Frame(self.content_frame)
        filter_frame.pack(fill=tk.X, pady=10)

        ttk.Label(filter_frame, text="Filter by Sport:").pack(side=tk.LEFT, padx=5)

        self.course_sport_filter = tk.StringVar()
        sport_filter = ttk.Combobox(filter_frame, textvariable=self.course_sport_filter,
                                    values=["All"] + sorted(
                                        list(set(course["sport"] for course in self.courses.values()))))
        sport_filter.pack(side=tk.LEFT, padx=5)
        sport_filter.set("All")

        ttk.Button(filter_frame, text="Apply Filter", style='Accent.TButton',
                   command=self.filter_courses).pack(side=tk.LEFT, padx=10)

        # Courses container
        self.courses_container = ttk.Frame(self.content_frame)
        self.courses_container.pack(fill=tk.BOTH, expand=True)

        # Show all courses initially
        self.filter_courses()

    def filter_courses(self):
        # Clear previous courses
        for widget in self.courses_container.winfo_children():
            widget.destroy()

        sport_filter = self.course_sport_filter.get()
        show_all = self.user_data.get("premium", False)

        filtered_courses = []
        for course in self.courses.values():
            if sport_filter == "All" or course["sport"] == sport_filter:
                if show_all or course["price"] <= 1000:  # Hide expensive courses for non-premium
                    filtered_courses.append(course)

        if not filtered_courses:
            no_results_frame = ttk.Frame(self.courses_container, style='Card.TFrame', padding=20)
            no_results_frame.pack(fill=tk.BOTH, expand=True, pady=20)

            ttk.Label(no_results_frame, text="No courses found matching your criteria",
                      font=('Arial', 12)).pack()
            return

        # Display courses in a grid
        rows = (len(filtered_courses) + 2) // 3  # 3 columns
        for i in range(rows):
            row_frame = ttk.Frame(self.courses_container)
            row_frame.pack(fill=tk.X, pady=5)

            for j in range(3):
                idx = i * 3 + j
                if idx >= len(filtered_courses):
                    break

                course = filtered_courses[idx]
                self.display_course_card(row_frame, course)

    def display_course_card(self, parent, course):
        card = ttk.Frame(parent, style='Card.TFrame', padding=10)
        card.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        # Course title
        ttk.Label(card, text=course["title"], font=('Arial', 12, 'bold'), wraplength=200).pack(anchor=tk.W)

        # Course info
        ttk.Label(card, text=f"Sport: {course['sport']}").pack(anchor=tk.W)
        ttk.Label(card, text=f"Duration: {course['duration']}").pack(anchor=tk.W)
        ttk.Label(card, text=f"Instructor: {course['instructor']}").pack(anchor=tk.W)

        # Rating
        ttk.Label(card, text=f"⭐ {course['rating']} ({course['students']} students)").pack(anchor=tk.W, pady=5)

        # Price and button
        price_frame = ttk.Frame(card)
        price_frame.pack(fill=tk.X, pady=5)

        if self.user_data.get("premium", False):
            price_text = "FREE (Premium)"
        else:
            price_text = f"₹{course['price']}"

        ttk.Label(price_frame, text=price_text, font=('Arial', 12, 'bold')).pack(side=tk.LEFT)

        btn_frame = ttk.Frame(price_frame)
        btn_frame.pack(side=tk.RIGHT)

        details_btn = ttk.Button(btn_frame, text="Details",
                                 command=lambda c=course: self.show_course_details(c))
        details_btn.pack(side=tk.LEFT, padx=2)

        if self.user_data.get("premium", False):
            enroll_text = "Enroll"
        else:
            enroll_text = "Enroll Now"

        enroll_btn = ttk.Button(btn_frame, text=enroll_text, style='Accent.TButton',
                                command=lambda c=course: self.enroll_in_course(c))
        enroll_btn.pack(side=tk.LEFT, padx=2)

    def show_course_details(self, course):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Course Details - {course['title']}")
        details_window.geometry("600x500")

        # Main container
        container = ttk.Frame(details_window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text=course["title"], font=('Arial', 16, 'bold')).pack(anchor=tk.W)
        ttk.Label(header_frame,
                  text=f"{course['sport']} | {course['duration']} | Instructor: {course['instructor']}").pack(
            anchor=tk.W)

        # Details frame
        details_frame = ttk.Frame(container)
        details_frame.pack(fill=tk.BOTH, expand=True)

        # Description
        desc_frame = ttk.LabelFrame(details_frame, text="Description", padding=10)
        desc_frame.pack(fill=tk.X, pady=5)

        ttk.Label(desc_frame, text=course["description"], wraplength=500).pack(anchor=tk.W)

        # Modules
        modules_frame = ttk.LabelFrame(details_frame, text="Course Modules", padding=10)
        modules_frame.pack(fill=tk.X, pady=5)

        for module in course["modules"]:
            ttk.Label(modules_frame, text=f"• {module}").pack(anchor=tk.W)

        # Price and enrollment
        action_frame = ttk.Frame(details_frame)
        action_frame.pack(fill=tk.X, pady=10)

        if self.user_data.get("premium", False):
            price_text = "FREE for Premium Members"
        else:
            price_text = f"Price: ₹{course['price']}"

        ttk.Label(action_frame, text=price_text, font=('Arial', 12, 'bold')).pack(side=tk.LEFT)

        enroll_btn = ttk.Button(action_frame, text="Enroll Now", style='Accent.TButton',
                                command=lambda: self.enroll_in_course(course, details_window))
        enroll_btn.pack(side=tk.RIGHT)

    def enroll_in_course(self, course, window=None):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to enroll in courses")
            return

        if self.user_data.get("premium", False):
            response = messagebox.askyesno("Enroll in Course",
                                           f"Enroll in '{course['title']}'?\n\n"
                                           "This course is free for Premium members.")
            if response:
                # Add to user's bookings
                booking = {
                    "type": "course",
                    "name": course["title"],
                    "sport": course["sport"],
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "status": "Enrolled"
                }

                self.users[self.current_user]["bookings"].append(booking)
                self.save_users()

                messagebox.showinfo("Enrolled",
                                    f"You have been enrolled in '{course['title']}'\n\n"
                                    "Check your email for access details.")
                if window:
                    window.destroy()
        else:
            response = messagebox.askyesno("Enroll in Course",
                                           f"Enroll in '{course['title']}' for ₹{course['price']}?")
            if response:
                # Add to user's bookings
                booking = {
                    "type": "course",
                    "name": course["title"],
                    "sport": course["sport"],
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "status": "Payment Pending"
                }

                self.users[self.current_user]["bookings"].append(booking)
                self.save_users()

                messagebox.showinfo("Payment",
                                    "Redirecting to payment gateway...\n\n"
                                    "After payment, you will receive course access details via email.")
                if window:
                    window.destroy()

    def show_webinars_page(self):
        self.clear_content_frame()

        ttk.Label(self.content_frame, text="Upcoming Webinars", style='Header.TLabel').pack(pady=10)

        # Search and filter frame
        filter_frame = ttk.Frame(self.content_frame)
        filter_frame.pack(fill=tk.X, pady=10)

        ttk.Label(filter_frame, text="Filter by Date:").pack(side=tk.LEFT, padx=5)

        self.webinar_date_filter = tk.StringVar()
        date_filter = ttk.Combobox(filter_frame, textvariable=self.webinar_date_filter,
                                   values=["All", "This Week", "Next Week", "This Month"])
        date_filter.pack(side=tk.LEFT, padx=5)
        date_filter.set("All")

        ttk.Button(filter_frame, text="Apply Filter", style='Accent.TButton',
                   command=self.filter_webinars).pack(side=tk.LEFT, padx=10)

        # Webinars container
        self.webinars_container = ttk.Frame(self.content_frame)
        self.webinars_container.pack(fill=tk.BOTH, expand=True)

        # Show all webinars initially
        self.filter_webinars()

    def filter_webinars(self):
        # Clear previous webinars
        for widget in self.webinars_container.winfo_children():
            widget.destroy()

        date_filter = self.webinar_date_filter.get()

        # In a real app, we would filter by actual dates
        filtered_webinars = list(self.webinars.values())

        if not filtered_webinars:
            no_results_frame = ttk.Frame(self.webinars_container, style='Card.TFrame', padding=20)
            no_results_frame.pack(fill=tk.BOTH, expand=True, pady=20)

            ttk.Label(no_results_frame, text="No webinars found matching your criteria",
                      font=('Arial', 12)).pack()
            return

        # Display webinars
        for webinar in filtered_webinars:
            self.display_webinar_card(webinar)

    def display_webinar_card(self, webinar):
        card = ttk.Frame(self.webinars_container, style='Card.TFrame', padding=10)
        card.pack(fill=tk.X, pady=5)

        # Webinar info
        info_frame = ttk.Frame(card)
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Label(info_frame, text=webinar["title"], font=('Arial', 12, 'bold')).pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Date: {webinar['date']} | Time: {webinar['time']}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Instructor: {webinar['instructor']}").pack(anchor=tk.W)
        ttk.Label(info_frame,
                  text=f"Seats available: {webinar['seats'] - webinar['registered']}/{webinar['seats']}").pack(
            anchor=tk.W)

        # Price and button
        price_frame = ttk.Frame(card)
        price_frame.pack(side=tk.RIGHT)

        ttk.Label(price_frame, text=f"₹{webinar['price']}", font=('Arial', 12, 'bold')).pack()

        btn_frame = ttk.Frame(price_frame)
        btn_frame.pack(pady=5)

        details_btn = ttk.Button(btn_frame, text="Details",
                                 command=lambda w=webinar: self.show_webinar_details(w))
        details_btn.pack(side=tk.LEFT, padx=2)

        book_btn = ttk.Button(btn_frame, text="Book Now", style='Accent.TButton',
                              command=lambda w=webinar: self.book_webinar(w))
        book_btn.pack(side=tk.LEFT, padx=2)

    def show_webinar_details(self, webinar):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Webinar Details - {webinar['title']}")
        details_window.geometry("500x400")

        # Main container
        container = ttk.Frame(details_window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text=webinar["title"], font=('Arial', 16, 'bold')).pack(anchor=tk.W)
        ttk.Label(header_frame, text=f"{webinar['date']} | {webinar['time']} | {webinar['duration']}").pack(anchor=tk.W)
        ttk.Label(header_frame, text=f"Instructor: {webinar['instructor']}").pack(anchor=tk.W)

        # Description
        desc_frame = ttk.LabelFrame(container, text="Description", padding=10)
        desc_frame.pack(fill=tk.X, pady=5)

        ttk.Label(desc_frame, text=webinar["description"], wraplength=400).pack(anchor=tk.W)

        # Seats info
        seats_frame = ttk.Frame(container)
        seats_frame.pack(fill=tk.X, pady=5)

        seats_available = webinar["seats"] - webinar["registered"]
        ttk.Label(seats_frame, text=f"Seats available: {seats_available}/{webinar['seats']}",
                  font=('Arial', 10, 'bold')).pack(side=tk.LEFT)

        # Price and booking
        action_frame = ttk.Frame(container)
        action_frame.pack(fill=tk.X, pady=10)

        ttk.Label(action_frame, text=f"Price: ₹{webinar['price']}", font=('Arial', 12, 'bold')).pack(side=tk.LEFT)

        book_btn = ttk.Button(action_frame, text="Book Now", style='Accent.TButton',
                              command=lambda: self.book_webinar(webinar, details_window))
        book_btn.pack(side=tk.RIGHT)

    def book_webinar(self, webinar, window=None):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to book webinars")
            return

        seats_available = webinar["seats"] - webinar["registered"]
        if seats_available <= 0:
            messagebox.showerror("Error", "This webinar is fully booked")
            return

        response = messagebox.askyesno("Confirm Booking",
                                       f"Book '{webinar['title']}' for ₹{webinar['price']}?\n\n"
                                       f"Date: {webinar['date']}\n"
                                       f"Time: {webinar['time']}")
        if response:
            # Add to user's bookings
            booking = {
                "type": "webinar",
                "name": webinar["title"],
                "date": webinar["date"],
                "time": webinar["time"],
                "price": webinar["price"],
                "status": "Confirmed"
            }

            self.users[self.current_user]["bookings"].append(booking)
            self.save_users()

            # Update webinar registration count (in a real app, this would be in a database)
            webinar["registered"] += 1

            messagebox.showinfo("Booking Confirmed",
                                f"You have successfully booked '{webinar['title']}'\n\n"
                                "Webinar link will be sent to your email 1 hour before the session.")
            if window:
                window.destroy()

    def show_equipment_page(self):
        self.clear_content_frame()

        ttk.Label(self.content_frame, text="Sports Equipment Store", style='Header.TLabel').pack(pady=10)

        # Search and filter frame
        filter_frame = ttk.Frame(self.content_frame)
        filter_frame.pack(fill=tk.X, pady=10)

        ttk.Label(filter_frame, text="Filter by Category:").pack(side=tk.LEFT, padx=5)

        self.equip_category_filter = tk.StringVar()
        category_filter = ttk.Combobox(filter_frame, textvariable=self.equip_category_filter,
                                       values=["All"] + sorted(
                                           list(set(item["category"] for item in self.equipment.values()))))
        category_filter.pack(side=tk.LEFT, padx=5)
        category_filter.set("All")

        ttk.Button(filter_frame, text="Apply Filter", style='Accent.TButton',
                   command=self.filter_equipment).pack(side=tk.LEFT, padx=10)

        # Equipment container
        self.equipment_container = ttk.Frame(self.content_frame)
        self.equipment_container.pack(fill=tk.BOTH, expand=True)

        # Show all equipment initially
        self.filter_equipment()

    def filter_equipment(self):
        # Clear previous equipment
        for widget in self.equipment_container.winfo_children():
            widget.destroy()

        category_filter = self.equip_category_filter.get()

        filtered_equipment = []
        for item in self.equipment.values():
            if category_filter == "All" or item["category"] == category_filter:
                filtered_equipment.append(item)

        if not filtered_equipment:
            no_results_frame = ttk.Frame(self.equipment_container, style='Card.TFrame', padding=20)
            no_results_frame.pack(fill=tk.BOTH, expand=True, pady=20)

            ttk.Label(no_results_frame, text="No equipment found matching your criteria",
                      font=('Arial', 12)).pack()
            return

        # Display equipment in a grid
        rows = (len(filtered_equipment) + 2) // 3  # 3 columns
        for i in range(rows):
            row_frame = ttk.Frame(self.equipment_container)
            row_frame.pack(fill=tk.X, pady=5)

            for j in range(3):
                idx = i * 3 + j
                if idx >= len(filtered_equipment):
                    break

                item = filtered_equipment[idx]
                self.display_equipment_card(row_frame, item)

    def display_equipment_card(self, parent, item):
        card = ttk.Frame(parent, style='Card.TFrame', padding=10)
        card.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        # Item name
        ttk.Label(card, text=item["name"], font=('Arial', 11, 'bold'), wraplength=200).pack(anchor=tk.W)

        # Category
        ttk.Label(card, text=f"Category: {item['category']}").pack(anchor=tk.W)

        # Rating
        ttk.Label(card, text=f"⭐ {item['rating']}").pack(anchor=tk.W)

        # Price
        original_price = item["price"]
        discount_price = original_price * (100 - item["discount"]) / 100

        price_frame = ttk.Frame(card)
        price_frame.pack(fill=tk.X, pady=5)

        ttk.Label(price_frame, text=f"₹{original_price}",
                  font=('Arial', 9), foreground='gray').pack(side=tk.LEFT)
        ttk.Label(price_frame, text=f"₹{discount_price:.0f}",
                  font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=5)
        ttk.Label(price_frame, text=f"{item['discount']}% OFF",
                  font=('Arial', 9, 'bold'), foreground='green').pack(side=tk.LEFT)

        # Buttons
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill=tk.X)

        details_btn = ttk.Button(btn_frame, text="Details",
                                 command=lambda i=item: self.show_equipment_details(i))
        details_btn.pack(side=tk.LEFT, padx=2)

        cart_btn = ttk.Button(btn_frame, text="Add to Cart", style='Accent.TButton',
                              command=lambda i=item: self.add_to_cart(i))
        cart_btn.pack(side=tk.LEFT, padx=2)

    def show_equipment_details(self, item):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Equipment Details - {item['name']}")
        details_window.geometry("500x400")

        # Main container
        container = ttk.Frame(details_window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text=item["name"], font=('Arial', 16, 'bold')).pack(anchor=tk.W)
        ttk.Label(header_frame, text=f"Category: {item['category']}").pack(anchor=tk.W)
        ttk.Label(header_frame, text=f"⭐ {item['rating']} | Stock: {item['stock']}").pack(anchor=tk.W)

        # Price
        price_frame = ttk.Frame(container)
        price_frame.pack(fill=tk.X, pady=5)

        original_price = item["price"]
        discount_price = original_price * (100 - item["discount"]) / 100

        ttk.Label(price_frame, text=f"Original Price: ₹{original_price}",
                  font=('Arial', 10), foreground='gray').pack(anchor=tk.W)
        ttk.Label(price_frame, text=f"Discounted Price: ₹{discount_price:.0f}",
                  font=('Arial', 12, 'bold')).pack(anchor=tk.W)
        ttk.Label(price_frame, text=f"You save: ₹{original_price - discount_price:.0f} ({item['discount']}%)",
                  font=('Arial', 10, 'bold'), foreground='green').pack(anchor=tk.W)

        # Description
        desc_frame = ttk.LabelFrame(container, text="Description", padding=10)
        desc_frame.pack(fill=tk.X, pady=5)

        ttk.Label(desc_frame, text=item["description"], wraplength=400).pack(anchor=tk.W)

        # Action buttons
        action_frame = ttk.Frame(container)
        action_frame.pack(fill=tk.X, pady=10)

        cart_btn = ttk.Button(action_frame, text="Add to Cart", style='Accent.TButton',
                              command=lambda: self.add_to_cart(item, details_window))
        cart_btn.pack(side=tk.RIGHT)

    def add_to_cart(self, item, window=None):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to add items to cart")
            return

        # In a real app, we would have a proper cart system
        messagebox.showinfo("Added to Cart",
                            f"{item['name']} has been added to your cart.\n\n"
                            "Proceed to checkout from your profile page.")
        if window:
            window.destroy()

    def show_upgrade_page(self):
        self.clear_content_frame()

        ttk.Label(self.content_frame, text="Upgrade to Premium", style='Header.TLabel').pack(pady=10)

        if self.user_data.get("premium", False):
            # Already premium member
            premium_frame = ttk.Frame(self.content_frame, style='Card.TFrame', padding=20)
            premium_frame.pack(fill=tk.BOTH, expand=True, pady=20)

            ttk.Label(premium_frame, text="You are already a Premium Member!",
                      font=('Arial', 14, 'bold'), style='Success.TLabel').pack(pady=10)

            ttk.Label(premium_frame,
                      text="Thank you for being a valued premium member. Enjoy all the exclusive benefits!",
                      font=('Arial', 11)).pack(pady=5)

            ttk.Label(premium_frame,
                      text="Your premium membership will automatically renew on your anniversary date.",
                      font=('Arial', 10)).pack(pady=5)

            cancel_btn = ttk.Button(premium_frame, text="Cancel Subscription", style='Danger.TButton',
                                    command=self.cancel_premium)
            cancel_btn.pack(pady=20)

            return

        # Benefits
        benefits_frame = ttk.LabelFrame(self.content_frame, text="Premium Benefits", padding=15)
        benefits_frame.pack(fill=tk.X, pady=10, padx=10)

        benefits = [
            "🎯 Access to all premium courses (₹5000+ value)",
            "🎤 Exclusive webinars with professionals",
            "🔍 Personalized academy recommendations",
            "📞 Priority customer support",
            "🏟️ 3D academy views and virtual tours",
            "📝 No registration fees for academies",
            "🛒 10% discount on sports equipment",
            "📱 Early access to new features"
        ]

        for benefit in benefits:
            ttk.Label(benefits_frame, text=benefit, font=('Arial', 11)).pack(anchor=tk.W, pady=2)

        # Pricing options
        pricing_frame = ttk.Frame(self.content_frame)
        pricing_frame.pack(pady=20)

        # Monthly option
        monthly_card = ttk.Frame(pricing_frame, style='Card.TFrame', padding=15)
        monthly_card.grid(row=0, column=0, padx=10, sticky=tk.NSEW)

        ttk.Label(monthly_card, text="Monthly", font=('Arial', 14, 'bold')).pack()
        ttk.Label(monthly_card, text="₹499/month", font=('Arial', 16)).pack(pady=5)
        ttk.Label(monthly_card, text="Flexible membership", font=('Arial', 10)).pack()

        ttk.Button(monthly_card, text="Choose Monthly", style='Accent.TButton',
                   command=lambda: self.process_upgrade("monthly")).pack(pady=10)

        # Yearly option (recommended)
        yearly_card = ttk.Frame(pricing_frame, style='Card.TFrame', padding=15)
        yearly_card.grid(row=0, column=1, padx=10, sticky=tk.NSEW)

        # Highlight recommended
        ttk.Label(yearly_card, text="Yearly (Recommended)", font=('Arial', 14, 'bold'),
                  foreground='#27ae60').pack()
        ttk.Label(yearly_card, text="₹4,999/year", font=('Arial', 16)).pack(pady=5)
        ttk.Label(yearly_card, text="Save ₹989 (2 months free)", font=('Arial', 10)).pack()

        ttk.Button(yearly_card, text="Choose Yearly", style='Premium.TButton',
                   command=lambda: self.process_upgrade("yearly")).pack(pady=10)

        # Configure grid weights
        pricing_frame.columnconfigure(0, weight=1)
        pricing_frame.columnconfigure(1, weight=1)

        # Testimonials
        testimonials_frame = ttk.LabelFrame(self.content_frame, text="What Our Premium Members Say", padding=10)
        testimonials_frame.pack(fill=tk.X, pady=10)

        testimonial = random.choice(self.testimonials)
        ttk.Label(testimonials_frame, text=f"\"{testimonial['text']}\"",
                  font=('Arial', 10, 'italic'), wraplength=600).pack()
        ttk.Label(testimonials_frame, text=f"- {testimonial['name']}",
                  font=('Arial', 9, 'bold')).pack(anchor=tk.E, pady=(5, 0))

    def process_upgrade(self, plan):
        if plan == "monthly":
            price = 499
            duration = "1 month"
        else:
            price = 4999
            duration = "1 year"

        response = messagebox.askyesno("Confirm Upgrade",
                                       f"Upgrade to Premium Membership for ₹{price} ({duration})?\n\n"
                                       "You will be redirected to our secure payment gateway.")
        if response:
            # Simulate payment processing
            self.root.after(1500, lambda: self.complete_upgrade(plan))
            messagebox.showinfo("Processing", "Redirecting to secure payment gateway...")

    def complete_upgrade(self, plan):
        self.users[self.current_user]["premium"] = True
        self.user_data["premium"] = True

        # Record subscription date
        today = datetime.now().strftime("%Y-%m-%d")
        self.users[self.current_user]["premium_since"] = today
        if plan == "yearly":
            self.users[self.current_user]["premium_until"] = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")

        self.save_users()

        messagebox.showinfo("Upgrade Complete",
                            "Thank you for upgrading to Premium!\n\n"
                            "Your premium benefits are now active. Enjoy your membership!")
        self.show_upgrade_page()  # Refresh the page

    def cancel_premium(self):
        response = messagebox.askyesno("Cancel Subscription",
                                       "Are you sure you want to cancel your premium subscription?\n\n"
                                       "You will lose access to premium benefits at the end of your billing period.")
        if response:
            # In a real app, we would schedule the cancellation
            self.users[self.current_user]["premium_auto_renew"] = False
            self.save_users()

            messagebox.showinfo("Subscription Cancelled",
                                "Your premium subscription will not renew.\n\n"
                                "You can continue to enjoy premium benefits until the end of your billing period.")
            self.show_upgrade_page()  # Refresh the page

    def show_profile(self):
        if not self.current_user:
            messagebox.showerror("Error", "Please login to view your profile")
            return

        profile_window = tk.Toplevel(self.root)
        profile_window.title(f"Profile - {self.current_user}")
        profile_window.geometry("600x500")

        # Main container
        container = ttk.Frame(profile_window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text="My Profile", font=('Arial', 16, 'bold')).pack(anchor=tk.W)

        # User info
        info_frame = ttk.LabelFrame(container, text="Account Information", padding=10)
        info_frame.pack(fill=tk.X, pady=5)

        user_info = [
            ("Username:", self.current_user),
            ("Name:", self.user_data.get("full_name", "Not provided")),
            ("Email:", self.user_data.get("email", "Not provided")),
            ("Phone:", self.user_data.get("phone", "Not provided")),
            ("Member since:", self.user_data.get("joined", "Unknown")),
            ("Status:", "Premium Member" if self.user_data.get("premium", False) else "Standard Member")
        ]

        for i, (label, value) in enumerate(user_info):
            ttk.Label(info_frame, text=label, font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky=tk.E, padx=5,
                                                                               pady=2)
            ttk.Label(info_frame, text=value).grid(row=i, column=1, sticky=tk.W, pady=2)

        # Bookings/Registrations
        bookings_frame = ttk.LabelFrame(container, text="My Bookings & Registrations", padding=10)
        bookings_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        if not self.user_data.get("bookings", []):
            ttk.Label(bookings_frame, text="You have no bookings yet.").pack(pady=20)
        else:
            # Create a treeview to display bookings
            columns = ("type", "name", "date", "status")
            tree = ttk.Treeview(bookings_frame, columns=columns, show="headings")

            # Define headings
            tree.heading("type", text="Type")
            tree.heading("name", text="Name")
            tree.heading("date", text="Date")
            tree.heading("status", text="Status")

            # Add data
            for booking in self.user_data.get("bookings", []):
                tree.insert("", tk.END, values=(
                    booking.get("type", ""),
                    booking.get("name", ""),
                    booking.get("date", ""),
                    booking.get("status", "")
                ))

            tree.pack(fill=tk.BOTH, expand=True)

        # Close button
        close_btn = ttk.Button(container, text="Close", command=profile_window.destroy)
        close_btn.pack(pady=10)

    def show_about_dialog(self):
        about_text = (
            "ACADINFO - Sports Academy Platform\n"
            "Version 2.0\n\n"
            "Our mission is to connect sports aspirants with the best training academies "
            "and provide online learning resources to help them achieve their dreams.\n\n"
            "© 2023 ACADINFO. All rights reserved."
        )
        messagebox.showinfo("About ACADINFO", about_text)

    def show_contact_dialog(self):
        contact_info = (
            "ACADINFO Support\n\n"
            "Email: support@acadinfo.com\n"
            "Phone: +91 9162960922\n"
            "Address: 123 Sports Avenue, New Delhi, India\n\n"
            "Office Hours: 9:00 AM - 6:00 PM (Mon-Sat)"
        )
        messagebox.showinfo("Contact Support", contact_info)

    def show_user_guide(self):
        guide_text = (
            "ACADINFO User Guide\n\n"
            "1. Find Academies: Search for sports academies by location and sport\n"
            "2. Courses: Enroll in online courses to improve your skills\n"
            "3. Webinars: Book live sessions with sports professionals\n"
            "4. Equipment: Purchase quality sports gear with member discounts\n"
            "5. Premium Membership: Unlock exclusive features and benefits\n\n"
            "For more help, please contact our support team."
        )
        messagebox.showinfo("User Guide", guide_text)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AcadInfoApp(root)
    root.mainloop()

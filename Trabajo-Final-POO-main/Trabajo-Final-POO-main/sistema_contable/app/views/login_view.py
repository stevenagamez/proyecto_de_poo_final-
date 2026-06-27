import customtkinter as ctk
from tkinter import messagebox

class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Inicio de Sesión - Sistema Contable")
        self.geometry("400x300")
        
        # Elementos de la interfaz (Etiquetas y campos de texto)
        self.label_title = ctk.CTkLabel(self, text="Iniciar Sesión", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)
        
        self.txt_user = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.txt_user.pack(pady=10)
        
        self.txt_pass = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.txt_pass.pack(pady=10)
        
        self.btn_login = ctk.CTkButton(self, text="Ingresar", command=self.verificar_credenciales)
        self.btn_login.pack(pady=20)

    def verificar_credenciales(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        
        # Llamamos al controlador para validar la autenticación
        usuario_valido = self.controller.autenticar_usuario(username, password)
        
        if usuario_valido:
            messagebox.showinfo("Éxito", f"Bienvenido, {username}")
            self.destroy() # Cierra la ventana de login y abre el dashboard
            
            # Importación local para evitar bucles de dependencias
            from app.views.dashboard_view import DashboardView
            dashboard = DashboardView(self.controller, username)
            dashboard.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
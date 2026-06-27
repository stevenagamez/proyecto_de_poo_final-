import customtkinter as ctk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class DashboardView(ctk.CTk):
    def __init__(self, controller, usuario_actual):
        super().__init__()
        self.controller = controller
        self.usuario_actual = usuario_actual
        self.title("Sistema Contable Profesional - Módulo Principal")
        self.geometry("1100x650")

        # Configuración de grilla MVC para separar responsabilidades
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.crear_formulario()
        self.crear_tabla_y_grafico()
        self.cargar_datos_tabla()

    def crear_formulario(self):
        frame_form = ctk.CTkFrame(self, width=300)
        frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_form, text="Asentar Póliza", font=("Arial", 16, "bold")).pack(pady=10)

        self.txt_concepto = ctk.CTkEntry(frame_form, placeholder_text="Concepto")
        self.txt_concepto.pack(pady=5)

        # Listas desplegables simulando el catálogo de cuentas (Modelo)
        self.cb_debe = ctk.CTkComboBox(frame_form, values=["1105 - Caja", "1110 - Bancos", "4135 - Ingresos"])
        self.cb_debe.pack(pady=5)
        self.cb_debe.set("1105 - Caja")

        self.cb_haber = ctk.CTkComboBox(frame_form, values=["1105 - Caja", "1110 - Bancos", "4135 - Ingresos"])
        self.cb_haber.pack(pady=5)
        self.cb_haber.set("1110 - Bancos")

        self.txt_monto = ctk.CTkEntry(frame_form, placeholder_text="Monto")
        self.txt_monto.pack(pady=5)

        btn_registrar = ctk.CTkButton(frame_form, text="Registrar Asiento", command=self.registrar_asiento)
        btn_registrar.pack(pady=15)

    def crear_tabla_y_grafico(self):
        frame_principal = ctk.CTkFrame(self)
        frame_principal.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        frame_principal.grid_rowconfigure(0, weight=1)
        frame_principal.grid_columnconfigure(0, weight=1)

        # Tabla (Treeview) para mostrar el libro diario
        self.tabla = ttk.Treeview(frame_principal, columns=("Fecha", "Concepto", "Debe", "Haber", "Monto", "Usuario"), show="headings")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Concepto", text="Concepto")
        self.tabla.heading("Debe", text="Cuenta Debe")
        self.tabla.heading("Haber", text="Cuenta Haber")
        self.tabla.heading("Monto", text="Monto")
        self.tabla.heading("Usuario", text="Usuario")
        
        self.tabla.column("Fecha", width=100)
        self.tabla.column("Concepto", width=150)
        self.tabla.column("Debe", width=120)
        self.tabla.column("Haber", width=120)
        self.tabla.column("Monto", width=100)
        self.tabla.column("Usuario", width=80)
        
        self.tabla.pack(fill="both", expand=True, pady=10)

        # Marco para el gráfico de Matplotlib
        self.chart_frame = ctk.CTkFrame(frame_principal, height=200)
        self.chart_frame.pack(fill="x", pady=10)
        self.generar_grafico_basico()

    def registrar_asiento(self):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        concepto = self.txt_concepto.get()
        debe = self.cb_debe.get()
        haber = self.cb_haber.get()
        monto = self.txt_monto.get()

        # El controlador procesa la solicitud instanciando el modelo "Poliza"
        try:
            monto_val = float(monto)
            self.controller.registrar_poliza(fecha, concepto, debe, haber, monto_val, self.usuario_actual)
            messagebox.showinfo("Éxito", "Póliza registrada correctamente.")
            self.limpiar_campos()
            self.cargar_datos_tabla()
            self.generar_grafico_basico()
        except ValueError as e:
            messagebox.showerror("Error en el monto", str(e))

    def limpiar_campos(self):
        self.txt_concepto.delete(0, 'end')
        self.txt_monto.delete(0, 'end')

    def cargar_datos_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        registros = self.controller.obtener_polizas()
        for reg in registros:
            self.tabla.insert("", "end", values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6]))

    def generar_grafico_basico(self):
        # Limpiamos el frame previo
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Obtenemos los montos y conceptos para el gráfico de barras usando matplotlib
        polizas = self.controller.obtener_polizas()
        conceptos = [p[2][:15] + "..." if len(p[2]) > 15 else p[2] for p in polizas[-5:]]
        montos = [p[5] for p in polizas[-5:]]

        fig, ax = plt.subplots(figsize=(6, 1.8))
        fig.patch.set_facecolor('#212121')
        ax.set_facecolor('#212121')
        
        if conceptos and montos:
            ax.bar(conceptos, montos, color='#1f77b4')
        
        ax.tick_params(colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title("Últimos asientos contables", color='white')
        
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)
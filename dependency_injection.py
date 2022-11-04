class ProcesadorPaypal:
    def realizar_pago(self) -> None:
        print("-> Pago haciendo uso de PayPal")

class ProcesadorStripe:
    def realizar_pago(self) -> None:
        print("-> Pago haciendo uso de Stripe")

# Procesamiento de pagos

class Pago:
    def __init__(self, procesador: ProcesadorPaypal) -> None:
        self.procesador = procesador

    def pago(self) -> None:
        self.procesador.realizar_pago()
    
class Pago:
    def __init__(self, procesador: ProcesadorStripe) -> None:
        self.procesador = procesador
    
    def pago(self) -> None:
        self.procesador.realizar_pago()
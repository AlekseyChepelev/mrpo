from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    invoice_id: int
    apartment_id: int
    service_id: int
    price: float

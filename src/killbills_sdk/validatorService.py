from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError, conint, constr, model_validator,PositiveFloat, PositiveInt
import re
from enum import Enum

class ReceiptFormat(str, Enum):
    JSON = 'json'
    PDF = 'pdf'
    SVG = 'svg'
    PNG = 'png'

class Payment(BaseModel):
    bin: int= None
    last_four: str = None
    auth_code: str = None
    scheme: str = None
    transaction_id: str = None

class Transaction(BaseModel):
    reference_id: str
    amount: PositiveInt
    customer_id: str
    transaction_date: PositiveInt
    store_name: str = None
    billing_descriptor: str
    siret: str = None
    currency: str = 'EUR'
    pos_name: str = None
    merchant_name: str = None
    payment: Payment = None
    @validator('siret')
    def validate_siret_digits(cls, value):
        if value is not None and not value.isdigit():
            raise ValueError('SIRET number must contain only digits')
        return value

class TransactionPayload(BaseModel):
    bank_id: constr(min_length=36, max_length=36)
    callback_url: str
    partner_name: str
    receipt_format: ReceiptFormat
    transaction: Transaction



class ReceiptPayload(BaseModel):
    reference_id: str
    amount: float
    currency: str
    date: str
    covers: Optional[int]
    table: Optional[str]
    invoice: Optional[int]
    total_discount: Optional[int] = None
    mode: Optional[int]
    partner_name: str
    merchant: Optional[dict]
    store: Optional[dict]
    taxes: Optional[List[dict]]
    items: Optional[List[dict]]
    payments: Optional[List[dict]]
    total_tax_amount: int = None
    @validator('date')
    def validate_date(cls, value):
        if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', value):
            raise ValueError('Invalid date format. Expected format: YYYY-MM-DDTHH:mm:ss')
        return value
    @validator('amount')
    def amount_non_negative(cls, value):
        if value < 0:
            raise ValueError('Amount cannot be negative')
        return value

    @validator('currency')
    def validate_currency(cls, value):
        if value not in ['EUR', 'USD']:
            raise ValueError('Invalid currency. Expected currency: EUR or USD')
        return value

    @validator('taxes', 'items', 'payments')
    def validate_list_items(cls, value):
        if value is not None and not isinstance(value, list):
            raise ValueError('Expected a list')
        return value

    @validator('siret',check_fields=False)
    def validate_siret(cls, value):
        if value and (len(value) != 14 or not value.isdigit()):
            raise ValueError('Invalid SIRET number. Expected 14 digits.')
        return value

    @validator('taxes', pre=True)
    def validate_tax_rate(cls, value):
        for tax in value:
            if 'rate' in tax and tax['rate'] not in [550, 1000, 2000]:
                raise ValueError('Invalid tax rate. Expected 550, 1000, or 2000')
        return value


def validate_transaction_payload(payload):
    if not payload:
        raise ValueError('No payload to validate')
    TransactionPayload(**payload)
    return True



def validate_receipt_payload(payload):
    if not payload:
        raise ValueError('No payload to validate')
    ReceiptPayload(**payload)
    return True


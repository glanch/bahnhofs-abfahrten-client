from enum import Enum


class SubscrChannelCustomerTypeOptionType(str, Enum):
    CUSTOMER_TYPE = "CUSTOMER_TYPE"

    def __str__(self) -> str:
        return str(self.value)

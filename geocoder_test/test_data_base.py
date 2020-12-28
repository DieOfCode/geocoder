from decimal import Decimal

from typing import List


class TestCursor:

    def execute(self, *args) -> bool:
        return True

    def fetchall(self) -> List[tuple]:
        return [('Ямайка', 'Бердяжки',
                 'улица Тургенева',
                 '4',
                 Decimal('56.841067'),
                 Decimal('60.614769')), ]


class TestDatabase:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return False

    def cursor(self) -> TestCursor:
        return TestCursor()

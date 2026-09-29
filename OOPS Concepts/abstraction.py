# Abstraction shows what an object can do while hiding how it does it.
# ABC and abstractmethod define the common interface for child classes.
from abc import ABC, abstractmethod

class FeaturePlan(ABC):
    """Abstract base class for applications with login functionality."""

    @abstractmethod
    def login(self):
        # Subclasses must provide the login implementation.
        pass

    @abstractmethod
    def logout(self):
        # Subclasses must provide the logout implementation.
        pass

class WebApp(FeaturePlan):
    """Concrete class that implements the abstract methods."""

    def login(self):
        print("I have logged in")

    def logout(self):
        print("I have logged out")

# WebApp can be instantiated because it implements every abstract method.
w = WebApp()
w.login()
w.logout()
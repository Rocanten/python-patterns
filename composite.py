from abc import ABC, abstractmethod

class Component(ABC):
	def __init__(self, name:str):
		self.name = name

	@abstractmethod
	def get_children(self)->list:
		pass

	@abstractmethod
	def add_child(self, child):
		pass

	@abstractmethod
	def remove_child(self, child):
		pass

class Leaf(Component):
	def get_children(self)->list:
		return []

	def add_child(self, child):
		raise RuntimeError("Leaf cannot have children")

	def remove_child(self, child):
		raise RuntimeError("Leaf cannot have children")

class Composite(Component):
	def __init__(self, children: list, name: str):
		super().__init__(name)
		self.children = children

	def add_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def get_children(self)->list:
		return self.children

def print_children(component: Component):
	for child in component.get_children():
		print(child.name)
		print_children(child)

leaf1 = Leaf('leaf 1')
composite1 = Composite([], 'composite 1')
composite2 = Composite([], 'composite 2')
leaf2 = Leaf('leaf 2')
leaf3 = Leaf('leaf 3')

composite1.add_child(leaf1)
composite1.add_child(leaf2)
composite1.add_child(composite2)
composite2.add_child(leaf3)

print_children(composite1)

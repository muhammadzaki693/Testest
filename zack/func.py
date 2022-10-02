import rich
import time
from rich.table import Table
from rich.console import Console

class Text:
	def table(headers, rows):
		console = Console()
		table = Table(show_header=True)
		for header in headers:
			table.add_column(header)
		table.add_row(*rows)
		console.print(table)
	
	def status(msg_doing, msg_complete ,msg_done, tasks):
		console = Console()
		
		with console.status(msg_doing) as st:
			while tasks:
				task = tasks.pop(0)
				time.sleep(1)
				console.log(task + " " + msg_complete)
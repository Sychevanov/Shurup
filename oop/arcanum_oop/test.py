DialogLine = namedtuple("DialogLine", ["text", "next_state"])
line = DialogLine("Привет", some_dialog_state)
print(line.text)
Роман Сычеванов(МГН)Сегодня, в 18:31
о прикольно
DmitryСегодня, в 18:32
@dataclass
class DialogLine:
  text: str
  next_state: DialogState
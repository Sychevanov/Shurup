Dmitry22.09.2020
startup_command выполянется, когда мы заходим в меню
before_select_command выполняется перед каждый показом меню
tear_down_command выполняется, когда мы выходим из меню
public void run() {
  if (startup_command != null) startup_command();
  while (isRunning) {
    if (before_select_command != null) before_select_command();
    показать меню
    выполнить связанный пункт меню
  }
  if (tear_down_command != null) tear_down_command();
}
Все что выше жто в меню должно быть в каком не помню

SelectStudentCommand должен вывести список стдуентов в кратком виде, позволить выбрать студента и сохранить выбранного студента в EditContext
ShowSelectedCommand -- вывести студента из EditContext на экран в расширенном виде
DeselectStudentCommand -- присвоить null студени

вызываем наши комманлы сеттерами


startup -- SelectStudentCommand
before_select -- ShowSelectedCommand
tear_down -- DeselectStudentCommand
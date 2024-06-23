Отчет по лабораторной работе: Сравнение алгоритмов поиска прямоугольников
Введение
В данной лабораторной работе рассматривались три алгоритма для поиска прямоугольников, содержащих заданную точку: BruteForceAlgorithm, MapAlgorithm и PersistentTreeAlgorithm. Целью работы было исследовать эффективность этих алгоритмов при увеличении количества прямоугольников.

Графики
График 1: Сравнение времени подготовки данных
График 2: Сравнение времени выполнения запросов
Анализ результатов
Время подготовки данных
BruteForceAlgorithm:

Демонстрирует наименьшее время подготовки данных, которое остается практически постоянным независимо от количества прямоугольников.
MapAlgorithm:

Время подготовки данных значительно увеличивается с ростом количества прямоугольников, особенно заметно для 32 и более прямоугольников.
PersistentTreeAlgorithm:

Время подготовки данных увеличивается умеренно, но наблюдается значительный рост при большем количестве прямоугольников (особенно от 32 до 64).
Время выполнения запросов
BruteForceAlgorithm:

Наихудшее время выполнения запросов среди всех трех алгоритмов, особенно при большом количестве запросов.
MapAlgorithm:

Хорошие результаты для небольшого количества запросов, но производительность снижается при увеличении числа запросов.
PersistentTreeAlgorithm:

Медленный рост времени выполнения запросов, что делает его наиболее эффективным для задач с большим количеством запросов.
Заключение
При увеличении количества прямоугольников время выполнения алгоритма на карте (MapAlgorithm) резко увеличивается из-за высокой асимптотической сложности построения карты - O(N^3). В худшем случае алгоритму может потребоваться выполнить N итераций по всей матрице размером N x N. Хотя построение персистентного дерева (PersistentTreeAlgorithm) на небольших наборах данных занимает примерно столько же времени, что и построение карты, алгоритм на дереве демонстрирует значительно более медленный рост времени выполнения с ростом количества данных. Это означает, что алгоритм на дереве может эффективно выполнять предварительную обработку даже для больших наборов прямоугольников, в отличие от алгоритма на карте.

На небольших наборах данных алгоритм полного перебора (BruteForceAlgorithm) может иметь небольшое преимущество, но оно настолько незначительно, что им можно пренебречь. При увеличении количества прямоугольников алгоритм полного перебора становится очень неэффективным, а алгоритмы с предварительной обработкой данных остаются относительно стабильными. MapAlgorithm превосходит PersistentTreeAlgorithm по эффективности, хотя оба имеют одинаковую теоретическую сложность. Это связано с тем, что алгоритму на дереве требуется выполнять дополнительный бинарный поиск и обход по дереву, что приводит к более высокому коэффициенту перед логарифмом по сравнению с алгоритмом на карте.

Рекомендации
BruteForceAlgorithm:

Рекомендуется для небольших наборов данных, так как не требует предварительной подготовки данных.
MapAlgorithm:

Обеспечивает удовлетворительную производительность для небольшого количества прямоугольников.
PersistentTreeAlgorithm:

Демонстрирует наилучшую производительность при работе с большими наборами данных и является предпочтительным для задач с большим количеством запросов.
Алгоритмы
MapAlgorithm
Препроцессинг: O(N^3)

Сжатие координат всех угловых точек прямоугольников по осям x и y.
Построение карты (матрицы) размером количество сжатых точек по оси x на количество сжатых точек по оси y.
Заполнение карты: обход всех прямоугольников и увеличение на единицу значения в ячейке карты, соответствующей сжатым координатам проекции каждого прямоугольника.
Поиск: O(M * logN)

Бинарный поиск сжатых координат точки запроса по осям x и y.
Обращение к ячейке карты, соответствующей найденным сжатым координатам.
PersistentTreeAlgorithm
Препроцессинг: O(N * logN)

Сжатие координат всех угловых точек прямоугольников по осям x и y.
Создание структуры Event, содержащей начало или конец существования прямоугольника и сжатые координаты.
Построение дерева отрезков на сжатых координатах.
Добавление в дерево отрезков персистентных узлов с использованием событий из структуры Event.
Поиск: O(M * logN)

Бинарный поиск сжатых координат точки запроса по осям x и y.
Нахождение нужного корня дерева отрезков по сжатым координатам точки запроса.
Обход дерева отрезков до нужного листа с использованием сжатых координат точки запроса.
Заключение
Алгоритм полного перебора лучше всего подходит для небольших наборов данных, так как он не требует предварительной подготовки данных. MapAlgorithm обеспечивает удовлетворительную производительность для небольшого количества прямоугольников. PersistentTreeAlgorithm демонстрирует наилучшую производительность при работе с большими наборами данных.

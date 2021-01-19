# Library system

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# Instrukcja Obsługi 

## Strona z punktu widzenia niezalogowanego użytkownika

Niezalogowany użytkownik ma dostęp do następujących widoków:
- Strona główna
![Strona główna](./images_readme/13.PNG)
* Wyszukiwanie książek. Istnieje możliwość filtrowana zasobów biblioteki po następujących kryteriach:
             * tytuł
             * autor
             * kategoria
             * połączenie kryteriów tytuł + kategoria lub autor + kategoria 
![Wyszukiwanie książek](./images_readme/1.PNG)

Po wyszukaniu konkretnej pozycji, możemy sprawdzić jej dostępność w różnych oddziałach
![Wyszukiwanie książek](./images_readme/14.PNG)
- Rejestracja
![Logowanie](./images_readme/2.PNG)
![Rejestracja](./images_readme/3.PNG)



## Strona z punktu widzenia zalogowanego użytkownika (czytelnika)

Po zalogowaniu do strony pod zakładka profil dostępną są informacje o zalogowanym użytkowniku:
![Konto użytkownika](./images_readme/12.PNG)
- dane osobowe
- kwota ewentualnych kar za zaległe książki
- wypożyczone książki


## Strona z punktu widzenia pracownika/admina
Jeśli zalogowany użytkownik ma uprawnienia administratorskie (jest pracownikiem biblioteki) to uzyskuje on dostęp do następujących opcji:
- możliwość dodawania nowych książek do zbiorów biblioteki
![Dodawanie książek](./images_readme/4.PNG)
- zarządzanie bieżącymi zbiorami poprzez możliwość zwiększania lub zmniejszania ilości egzemplarzy danej pozycji, usuwanie całej książki (wszystkich instancji) z zasobów biblioteki, automatyczne uzupełnianie formularza dodawania książek w przypadku gdy chcemy dodać książkę, która już istnieje w jednym oddziale, do innego
![Zarządzanie zasobami](./images_readme/5.PNG)
- dodawanie kont nowych pracowników
![Dodawanie pracowników](./images_readme/6.PNG)
![Dodawanie pracowników](./images_readme/7.PNG)
- dostęp do danych czytelników oraz możliwość usunięcia ich kont
![Zarządzanie użytkownikami](./images_readme/8.PNG)
- możliwość dodawania nowych oddziałów (fili biblioteki)
![Dodawanie oddziałów](./images_readme/9.PNG)
- możliwość wypożyczania książek
![Wypożyczanie książek](./images_readme/10.PNG)
- przyjmowanie zwrotów
![PRzyjmowanie zwrotów](./images_readme/11.PNG)
 

// Mateusz Olech 158997

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>

struct STUDENT {
    std::string im_nazwisko;
    float oceny[5];
    float srednia_ocen;
};

void wczytajDane(STUDENT* tablica, int n) {
    std::ifstream plik("dane.txt");
    if (!plik) {
        std::cout << "Błąd przy otwieraniu pliku dane.txt" << std::endl;
        return;
    }

    for (int i = 0; i < n; i++) {
        std::string imie_nazwisko;
        std::getline(plik, imie_nazwisko);
        tablica[i].im_nazwisko = imie_nazwisko;

        // Generowanie losowych ocen
        for (int j = 0; j < 5; j++) {
            int ocena = 2 + static_cast<int>(std::rand()) / (static_cast<int>(RAND_MAX / 3.5)); // Generowanie losowej oceny z zakresu 2-5
            tablica[i].oceny[j] = ocena;
        }
    }

    plik.close();
}

void obliczSrednia(STUDENT* tablica, int n) {
    for (int i = 0; i < n; i++) {
        float suma = 0;
        for (int j = 0; j < 5; j++) {
            suma += tablica[i].oceny[j];
        }
        tablica[i].srednia_ocen = suma / 5;
    }
}

float obliczSredniaOgolna(STUDENT* tablica, int n) {
    float suma = 0;
    for (int i = 0; i < n; i++) {
        suma += tablica[i].srednia_ocen;
    }
    return suma / n;
}

int ileStudentowPowSredniejOgolnej(STUDENT* tablica, int n, float srednia) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (tablica[i].srednia_ocen > srednia) {
            count++;
        }
    }
    return count;
}

void wypiszDane(STUDENT* tablica, int n) {
    for (int i = 0; i < n; i++) {
        std::cout << "Student " << i + 1 << ": " << tablica[i].im_nazwisko << std::endl;
        std::cout << "Oceny: ";
        for (int j = 0; j < 5; j++) {
            std::cout << tablica[i].oceny[j] << " ";
        }
        std::cout << std::endl;
        std::cout << "Średnia ocen: " << tablica[i].srednia_ocen << std::endl;
        std::cout << std::endl;
    }
}

void zapiszNajwyzszaSredniaDoPliku(STUDENT* tablica, int n) {
    float najwyzsza_srednia = tablica[0].srednia_ocen;
    int indeks_najwyzszej = 0;

    for (int i = 1; i < n; i++) {
        if (tablica[i].srednia_ocen > najwyzsza_srednia) {
            najwyzsza_srednia = tablica[i].srednia_ocen;
            indeks_najwyzszej = i;
        }
    }

    std::ofstream plik("najwyzsza_srednia.txt");
    if (!plik) {
        std::cout << "Błąd przy otwieraniu pliku najwyzsza_srednia.txt" << std::endl;
        return;
    }

    plik << "Student " << indeks_najwyzszej + 1 << ": " << tablica[indeks_najwyzszej].im_nazwisko << std::endl;
    plik << "Oceny: ";
    for (int j = 0; j < 5; j++) {
        plik << tablica[indeks_najwyzszej].oceny[j] << " ";
    }
    plik << std::endl;
    plik << "Średnia ocen: " << tablica[indeks_najwyzszej].srednia_ocen << std::endl;

    plik.close();
}

void wyszukajStudenta(STUDENT* tablica, int n, std::string imie_nazwisko) {
    for (int i = 0; i < n; i++) {
        if (tablica[i].im_nazwisko == imie_nazwisko) {
            std::cout << "Student " << i + 1 << ": " << tablica[i].im_nazwisko << std::endl;
            std::cout << "Oceny: ";
            for (int j = 0; j < 5; j++) {
                std::cout << tablica[i].oceny[j] << " ";
            }
            std::cout << std::endl;
            std::cout << "Średnia ocen: " << tablica[i].srednia_ocen << std::endl;
            return;
        }
    }
    std::cout << "Nie znaleziono studenta o podanym imieniu i nazwisku." << std::endl;
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    int n;
    std::cout << "Podaj liczbę studentów: ";
    std::cin >> n;

    STUDENT* tablica = new STUDENT[n];

    wczytajDane(tablica, n);
    obliczSrednia(tablica, n);
    float sredniaOgolna = obliczSredniaOgolna(tablica, n);
    int ilePowSredniejOgolnej = ileStudentowPowSredniejOgolnej(tablica, n, sredniaOgolna);

    std::cout << "Liczba studentów posiadających średnią ocen powyżej średniej wszystkich studentów: " << ilePowSredniejOgolnej << std::endl;

    std::cout << "Dane studentów:" << std::endl;
    wypiszDane(tablica, n);

    zapiszNajwyzszaSredniaDoPliku(tablica, n);

    std::string imie_nazwisko;
    std::cout << "Podaj imię i nazwisko studenta do wyszukania: ";
    std::cin.ignore(); // Ignorujemy znak nowej linii po wczytaniu liczby n
    std::getline(std::cin, imie_nazwisko);
    wyszukajStudenta(tablica, n, imie_nazwisko);

    delete[] tablica;

    return 0;
}

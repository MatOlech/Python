#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;

const int ROZMIAR = 6;

// Zadanie 1

void wypelnijTablice(int A[][ROZMIAR], int p, int k) {
    srand(time(NULL));

    for (int i = 0; i < ROZMIAR; i++) {
        for (int j = 0; j < ROZMIAR; j++) {
            A[i][j] = rand() % (k - p + 1) + p;
        }
    }
}

void wypiszTablice(const int A[][ROZMIAR]) {
    for (int i = 0; i < ROZMIAR; i++) {
        for (int j = 0; j < ROZMIAR; j++) {
            cout << setw(4) << A[i][j] << " ";
        }
        cout << endl;
    }
}

void zapiszTabliceDoPliku(const int A[][ROZMIAR], const string& nazwaPliku) {
    ofstream plik(nazwaPliku);
    if (plik.is_open()) {
        for (int i = 0; i < ROZMIAR; i++) {
            for (int j = 0; j < ROZMIAR; j++) {
                plik << A[i][j] << " ";
            }
            plik << endl;
        }
        plik.close();
    } else {
        cout << "Nie można otworzyć pliku." << endl;
    }
}

void odczytajTabliceZPliku(int A[][ROZMIAR], const string& nazwaPliku) {
    ifstream plik(nazwaPliku);
    if (plik.is_open()) {
        for (int i = 0; i < ROZMIAR; i++) {
            for (int j = 0; j < ROZMIAR; j++) {
                plik >> A[j][i];
            }
        }
        plik.close();
    } else {
        cout << "Nie można otworzyć pliku." << endl;
    }
}

// Zadanie 2

struct Pracownik {
    string nazwisko;
    int staz;
    double pensja;
};

void wypiszPracownikow(const vector<Pracownik>& pracownicy) {
    cout << "Nazwisko\tStaż\tPensja" << endl;
    for (const auto& pracownik : pracownicy) {
        cout << pracownik.nazwisko << "\t\t" << pracownik.staz << "\t" << pracownik.pensja << endl;
    }
}

double obliczSredniaPlace(const vector<Pracownik>& pracownicy, int minStaz) {
    double suma = 0.0;
    int licznik = 0;

    for (const auto& pracownik : pracownicy) {
        if (pracownik.staz > minStaz) {
            suma += pracownik.pensja;
            licznik++;
        }
    }

    if (licznik > 0) {
        return suma / licznik;
    } else {
        return 0.0;
    }
}

bool porownajPracownikow(const Pracownik& p1, const Pracownik& p2) {
    return p1.nazwisko < p2.nazwisko;
}

void sortujPracownikow(vector<Pracownik>& pracownicy) {
    sort(pracownicy.begin(), pracownicy.end(), porownajPracownikow);
}

void zapiszPracownikowDoPliku(const vector<Pracownik>& pracownicy, const string& nazwaPliku) {
    ofstream plik(nazwaPliku);
    if (plik.is_open()) {
        for (const auto& pracownik : pracownicy) {
            plik << pracownik.nazwisko << " " << pracownik.staz << " " << pracownik.pensja << endl;
        }
        plik.close();
    } else {
        cout << "Nie można otworzyć pliku." << endl;
    }
}

void wczytajPracownikowZPliku(vector<Pracownik>& pracownicy, const string& nazwaPliku) {
    ifstream plik(nazwaPliku);
    if (plik.is_open()) {
        pracownicy.clear();
        Pracownik pracownik;
        while (plik >> pracownik.nazwisko >> pracownik.staz >> pracownik.pensja) {
            pracownicy.push_back(pracownik);
        }
        plik.close();
    } else {
        cout << "Nie można otworzyć pliku." << endl;
    }
}

int main() {
    // Zadanie 1
    int A[ROZMIAR][ROZMIAR];
    int p, k;

    cout << "Podaj dolny zakres przedziału (p): ";
    cin >> p;
    cout << "Podaj górny zakres przedziału (k): ";
    cin >> k;

    wypelnijTablice(A, p, k);

    cout << "Tablica A:" << endl;
    wypiszTablice(A);

    zapiszTabliceDoPliku(A, "tablica.txt");

    int B[ROZMIAR][ROZMIAR];
    odczytajTabliceZPliku(B, "tablica.txt");

    cout << "Tablica B (odczytana z pliku):" << endl;
    wypiszTablice(B);

    // Zadanie 2
    int N;
    cout << "Podaj liczbę pracowników: ";
    cin >> N;

    vector<Pracownik> pracownicy(N);
    wczytajPracownikowZPliku(pracownicy, "pracownicy.txt");

    cout << "Dane pracowników:" << endl;
    wypiszPracownikow(pracownicy);

    int minStaz;
    cout << "Podaj minimalny staż pracy: ";
    cin >> minStaz;

    double sredniaPensja = obliczSredniaPlace(pracownicy, minStaz);
    cout << "Średnia pensja pracowników z dłuższym stażem niż " << minStaz << ": " << sredniaPensja << endl;

    sortujPracownikow(pracownicy);
    zapiszPracownikowDoPliku(pracownicy, "pracownicy_posortowani.txt");

    return 0;
}

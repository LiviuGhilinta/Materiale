	#include <iostream>
	#include <string>
	#include <cctype>
	using namespace std;
	
	int incercare = 0;
	bool game_over = false;
	
	void Informatii()
	{
		cout<<"Bine ati venit!"<<endl;
		cout<<"Acesta joc de tip ghiceste cuvantul!" <<endl;
		cout<<"Regulile sunt urmatoarele: Aveti 5 incercari sa ghiciti cuvantul!"<<endl;
		cout<<"Daca ghiciti o litera numarul de incercari nu va creste!"<<endl;
		cout<<"Daca nu ghiciti litera, numarul de incercari va creste!"<<endl;
		cout<<"Jocul este pe 5 nivele, puteti sa alegeti de la bun inceput nivelul dorit(0=Usor; 5= Greu)"<<endl;
	}
	
	void verificare(char alegere)
	{
		int a = alegere - '0' ;
		if(a < 0 || a >5)
		{
			cout<<"Regulile sunt Reguli. Game OVER!"<<endl;
			exit(-1);
		}
		else 
		{
			return;
		}
	}
	
	void desen(int incercare)
	{
		switch(incercare)
		{
			case 0 : 
					cout << " +---+" << endl;
	            	cout << " |   |" << endl;
	            	cout << "     |" << endl;
	            	cout << "     |" << endl;
	            	cout << "     |" << endl;
	            	cout << "     |" << endl;
	            	cout << "=========" << endl;
	            	break;
	        
	        case 1 : 
				cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << "     |" << endl;
	            cout << "     |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	            break;
	        
			case 2 : 
				cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << " |   |" << endl;
	            cout << "     |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	            break;
	        case 3:
	            cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << "/|   |" << endl;
	            cout << "     |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	            break;
	        case 4:
	            cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << "/|\\ |" << endl;
	            cout << "     |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	            break;
	        case 5:
	            cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << "/|\\ |" << endl;
	            cout << "/    |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	            break;
	        case 6:
				cout << " +---+" << endl;
	            cout << " |   |" << endl;
	            cout << " O   |" << endl;
	            cout << "/|\\ |" << endl;
	            cout << "/ \  |" << endl;
	            cout << "     |" << endl;
	            cout << "=========" << endl;
	                  
	    }
	}    
	
	
	void hint(string cuvant, string cuvant_ramas,bool hint)
	{
		int i = 0;
		int j = 0;
		int k = 0;
		int x = 0;
		char q;
		cout<<"Vreti ajutor?(y/n)"<<endl;
		cin>>q;
		q = tolower(q);
		char alfabet[26] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g',
	                          'h', 'i', 'j', 'k', 'l', 'm', 'n', 
	                          'o', 'p', 'q', 'r', 's', 't', 'u',
	                          'v', 'w', 'x', 'y', 'z' };
		if (q == 'y')
		{
			if (hint == false)
			{
				for(j=0; j<cuvant.length(); j++)
				{
					for(i = 0; i< 26; i++)
					{
						if(alfabet[i] == cuvant[j])
						{
							if(cuvant_ramas[j] == '*')
							{
								cout<<"Incercati:"<<alfabet[i]<<endl;
								hint = true;
								return;	
							}
							else
							{
								continue;
							}
						}
					}
				}
			}
			else
			{
				cout<<"Aveti voie doar la un singur hint!"<<endl;
				return;
			}
		}
		else if (q=='n')
		{
			return;
		}
		else
		{
			cout<<"Regulile sunt reguli!"<<endl;
			hint == true;
			cout<<"Ati pierdut dreptul de a primi un hint!"<<endl;
		}
		
	}
	
	
	
	string cautare_cuvant(string cuvant)
	{
		int i = 0;
		bool gasit = false;
		bool permisiune_hint = false;
		char alegere;
		string cuvant_ramas(cuvant.length(), '*');
		cout<<"Cuvantul cenzurat: "<<cuvant_ramas<<endl;
		bool hint_folosit = false;	
		while (incercare < 5)
		{
			cout<<"Alege litera: ";
			cin>>alegere;
			alegere = tolower(alegere);
			for (i=0 ; i<cuvant.length();i++)
				{
					if(alegere == cuvant[i])
					{
						cuvant_ramas[i] = alegere;
						gasit = true;
					}
					else
					{
						continue;
					}
					
				}
			if(gasit == true)
			{
				if(cuvant_ramas == cuvant)
				{
					desen(incercare);
					cout<<"Felicitari ati gasit cuvantul!"<<endl;
					return cuvant_ramas;
				}
				else
				{
					desen(incercare);
					cout<<"Ati gasit litera!"<<endl;
					permisiune_hint = true;
					cout<<cuvant_ramas<<endl;
					cout<<"Numarul de incercari ramase:"<<5-incercare<<endl;
					gasit = false;
				}
			}
			else if(gasit == false)
			{
				desen(incercare+1);
				cout<<"Nu ati gasit litera!Mai incercati!"<<endl;
				if(permisiune_hint == true)
				{
					if (hint_folosit == false && permisiune_hint == true)
					{
						hint(cuvant,cuvant_ramas,hint_folosit);
						hint_folosit = true;
					}
				/*	else
					{
						hint(cuvant,cuvant_ramas,hint_folosit);
					}*/
				}
				incercare+=1;
				cout<<"Numarul de incercari ramase: "<<5-incercare<<endl;
			}	
		}
		return cuvant_ramas;
	}
	
	int next_level(int nivel)
	{
		char q;
		cout<<"Doriti sa jucati si urmatorul nivel? (y/n)"<<endl;
		cin>>q;
		q = tolower(q);
		if(q == 'y')
		{
			if (nivel <5)
			{
				cout<<"Atentie cuvintele devin din ce in ce mai grele!"<<endl;
				incercare = 0;
				return nivel+1;
			}
			else
			{
				cout<<"Ati terminat jocul! Felicitari!"<<endl;
				exit(-1);
			}	
		}
		else if (q == 'n')
		{
			cout<<"Am inteles :(( Game OVER."<<endl;
			exit(-1);
		}
		else
		{
			cout<<"Ati gresit alegerea. Jocul se va oprii!"<<endl;
			exit(-1);
		}
				
	}
	
	
	int main()
	{
		Informatii();
		int i = 0;
		string a[] = {"text","fraza","cuvant","ceasca","fumator","paralelipiped"};
		char alegere ;
		int nivel = 0;
		cout<<"\nAlegeti nivelul(Va recomandam sa incepeti cu nivelul 0):";
		cin>>alegere;
		if(isdigit(alegere) == 1)
		{
			verificare(alegere);
			nivel = alegere - '0';
		}
		else
		{
			cout<<"Regulile sunt Reguli. Game Over!"<<endl;
			exit(-1);
		}
		desen(0);
		string cuvant;
		cuvant = cautare_cuvant(a[nivel]);
		cout<<"Cuvantul vostru: "<<cuvant<<", Cuvantul corect:" << a[nivel]<<endl;
		for(i = 0; i<4; i++)
			{
				if(incercare !=5)
				{
					nivel = next_level(nivel);
					desen(0);
					cuvant = cautare_cuvant(a[nivel]);
					cout<<"Cuvantul vostru: "<<cuvant<<", Cuvantul corect:" << a[nivel]<<endl;
				}
				else
				{
					cout<<"\nMultumim pentru ca ati incercat jocul nostru!"<<endl;
					exit(-1);
				}
			}

		
				return 0;
		
	}

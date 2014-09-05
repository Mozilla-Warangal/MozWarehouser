#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
	ifstream f("List.txt");
	char line[80]; // read line by line.
	while(f.getline(line,80)){
		char def_text[]="git clone https://github.com/";
		strcat(def_text,line);
		// DEBUG : cout<<def_text<<endl;
		system(def_text);
	}
	return 0;
}
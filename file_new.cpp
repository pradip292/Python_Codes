#include<iostream>
#include<fstream>
using namespace std;
struct info
{
	int rollno;
	char name[40];
	float percent;
}s;
int main()
{
	int c,ch,flag,rno;
	ofstream f,f1;
	f.open("stud.txt");
	ifstream ifs;
	do
	{
		cout<<"1.insert\n2.disaplay\n3.delete\n4.update\n";
		cout<<"enter your choice";
		cin>>ch;
		switch(ch)
		{
			case 1:
				do
				{
					cout<<"\n";
					cout<<"Enter roll no , name and percent ";
					cin>>s.rollno>>s.name>>s.percent;
					f<<"\t"<<s.rollno;
					f<<"\t"<<s.name;
					f<<"\t"<<s.percent;
					cout<<"do you want to continue";
					cin>>c;
				}while(c==1);
				cout<<"reocrd added successfully";
				f.close();
				break;
			case 2:
				{
					ifs.open("stud.txt");
					while(!ifs.eof())
					{
						ifs>>s.rollno;
						ifs>>s.name;
						ifs>>s.percent;
						cout<<"roll no"<<s.rollno;
						cout<<"name"<<s.name;
						cout<<"percent"<<s.percent;
					}
				}
				ifs.close();
				break;
			case 3:
				{
					f1.open("student.txt");
					ifs.open("stud.txt");
					cout<<"Enter the roll no which you want to delete";
					cin>>rno;
					flag=0;
					while(!ifs.eof())
					{
						ifs>>s.rollno;
						ifs>>s.name;
						ifs>>s.percent;
						if(rno==s.rollno)
						{
							flag=1;
							cout<<"Record is deleted";
						}
						else if(rno!=s.rollno)
						{
							f1<<s.rollno;
							f1<<s.name;
							f1<<s.percent;
						}
						
					}
					if(flag==0)
					cout<<"record is not present";
					remove("stud.txt");
					rename("student.txt","stud.txt");
					ifs.close();
					f1.close();
				}
			case 4:
				{
					f1.open("student.txt");
					ifs.open("stud.txt");
					cout<<"Enter the roll no which you want to update";
					cin>>rno;
					flag=0;
					while(!ifs.eof())
					{
						ifs>>s.rollno;
						ifs>>s.name;
						ifs>>s.percent;
						if(rno==s.rollno)
						{
							cout<<"Enter the roll no , name and percent";
							cin>>s.rollno>>s.name>>s.percent;
							f1<<s.rollno;
							f1<<s.name;
							f1<<s.percent;
							flag=1;
							
						}
						else if(rno!=s.rollno)
						{
							f1<<s.rollno;
							f1<<s.name;
							f1<<s.percent;
						}
						
					}
					ifs.close();
					f1.close();
					if(flag==0)
					cout<<"reord is not present";
					remove("stud.txt");
					rename("student.txt","stud.txt");
				}
				
		}
		cout<<"do you want to continue";
		cin>>c;
	}while(c==1);
	return 0;
}

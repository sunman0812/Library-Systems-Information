#include "BookInformation.h"

int main()
{
	Date d(2, 2, 2020);
	BookInformation b1;
	b1.setDueDate(d);
	b1.setPublishingDate(d);
	b1.print();
	cin.get();
}
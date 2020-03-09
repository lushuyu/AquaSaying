#include"json.hpp"
#include<iostream>
#include<fstream>
#include<iomanip>

using json = nlohmann::json;

int main() {
    // json newjson;

    // newjson["id"] = json::object();
    // newjson["auther"] = json::object();
    // newjson["text"] = json::object();

    // newjson["id"] = 1;

    // puts("Please type in the auther name.");
    // std::cin >> newjson["auther"];
    // puts("Good job.");
    // puts("Please input the text.");
    // std::cin >> newjson["text"];
    // puts("Good job.");
    // std::cout << std::setw(4) << newjson << std::endl;

    system("copy AquaSayinglist.json AquaSayinglisk_bak.json");
    std::ifstream input("AquaSayinglist.json");


    json AquaSayinglist;
    input >> AquaSayinglist;

    int siz;
    for (siz = 0; AquaSayinglist[siz]["id"] != nullptr; siz++) {
        std::cout << "已经发现 id = " << AquaSayinglist[siz]["id"] << std::endl;
    }

    //删除重复
    AquaSayinglist.erase(siz--);

    //选择菜单


    std::ofstream o("AquaSayinglist.json");
    o << std::setw(4) << AquaSayinglist << std::endl;
}
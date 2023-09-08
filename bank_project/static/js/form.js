
 var subcategory = {
            Trivandrum: ["Pattom", "Sreekariyam", "Chakkai"],
            Ernakulam: ["Kochi", "Aluva", "Perumbavoor"],
            Kannur: ["Chirakkal", "Payyanur", "Iritty"],
            Kozhikode: ["Beypoor", "Koilandi", "Balushery"],
            Malapuram: ["tirur", "Kottakkal", "Karipur"],
            Pattanmtita: ["Konni", "Adoor", "Panthalam"],

        }

        function makeSubmenu(value) {
            if (value.length == 0)
            document.getElementById("categorySelect").innerHTML = "<option></option>";
            else {
                var citiesOptions = "";
                for (categoryId in subcategory[value]) {
                    citiesOptions += "<option>" + subcategory[value][categoryId] + "</option>";
                }
                document.getElementById("categorySelect").innerHTML = citiesOptions;
            }
        }

        function displaySelected() {
            var country = document.getElementById("category").value;
            var city = document.getElementById("categorySelect").value;
            alert(country + "\n" + city);
        }

        function resetSelection() {
            document.getElementById("category").selectedIndex = 0;
            document.getElementById("categorySelect").selectedIndex = 0;
                }
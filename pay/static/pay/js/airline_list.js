function getList(){
                var element = document.getElementById("main-container");
                try{
                    element.parentNode.removeChild(element);
                }catch(exception){}

                var data = [
                        {flightname:"Delta Airines", departure:"10:40pm", arrival:"2:30am", trip: 'BOS->CHI  CHI->SFO'},
                        {flightname:"United Airlines", departure:"11:40pm", arrival:"1:30am", trip: 'BOS->SLC  SLC->SFO'}

                        ];
            var theTemplateScript = $('#airline-list-template').html();
            var theTemplate = Handlebars.compile(theTemplateScript);
                $('#airline-dataTable-container').append(theTemplate(data));
            }
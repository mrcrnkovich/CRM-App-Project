    <script>
            $(document).ready(function(){
                function getClients(){
                    $.get("http://127.0.0.1:5000/api/clients/lola", function(responseText){

                        data = responseText;
                        $('#t').empty();

                        for(i=0; i<data.clients.length; i++){
                            $('#t').append('<tr><th scope="row">'+(i+1)+'</th>'
                                + "<td>"+data.clients[i].first_name+"</td>"
                                + "<td>" +data.clients[i].last_name+"</td>"
                                + "<td>" +data.clients[i].email+"</td>"
                                + "<td> <div class='form-check'><input type='checkbox'"
                                + "class='form-check-input'></div>"
                                + '</tr>');
                        }

                        console.log($('#t').contents());
                    });
                };


                function getShowings(){
                    $.get("http://127.0.0.1:5000/api/showings/lola", function(responseText){

                        data = responseText;
                        $('#showings').empty();

                        for(i=0; i<data.Showings.length; i++){
                            $('#showings').append('<li class="list-group-item">'
                                + "Client: "
                                + data.Showings[i].last_name+", "
                                + data.Showings[i].first_name+" | "
                                + "Property: "
                                + data.Showings[i].Property_ID+" | "
                                + "Feeback: "
                                + data.Showings[i].Feedback+" | "
                                + "Rating: "
                                + data.Showings[i].Rating
                                + '</li>');
                        }

                        console.log($('#showings').contents());
                    });
                };

                getShowings();
                getClients();

                $('#rb').click(function(){getShowings()});
                $('#rb').click(function(){getClients()});
            });
    </script>

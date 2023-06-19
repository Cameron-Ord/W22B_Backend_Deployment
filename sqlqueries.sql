call new_client('Cameron', 'email@email.com', 'password', 'bio', 'image_input');
call client_login('token', 'Cameron', 'password'); 
call get_client('token'); 
call log_out('token'); 
call client_login('newtoken2', 'Matthew', 'password'); 
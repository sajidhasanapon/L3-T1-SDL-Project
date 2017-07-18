package app;


import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class LoginScreenController
{

    @FXML
    private TextField usernameBox;

    @FXML
    private PasswordField passwordBox;

    @FXML
    private Button signInButton;

    @FXML
    private Label msgLabel;

    @FXML
    void signIn(ActionEvent event)
    {
        String userAttempt = usernameBox.getText();
        String passAttempt = passwordBox.getText();

        System.out.println("Attempt" + '\n' + userAttempt + '\n' + passAttempt);
        System.out.println("\n\nRegistered:\n");

        try
        {
            File inputFile = new File("login");
            FileReader in = new FileReader(inputFile);
            BufferedReader br = new BufferedReader(in);

            String user = "", pass = "";
            while ((user = br.readLine()) != null)
            {
                pass = br.readLine();
                System.out.println(user + '\n' + pass);

                if(user.equals(userAttempt) && pass.equals(passAttempt))
                {
                    //successful
                    new HomeScreenMain(main.window, user, pass);

                    return;
                }
            }

            Alert alert = new Alert(Alert.AlertType.ERROR, "Incorrect username / password!");
            alert.showAndWait();


        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

    }

    LoginScreenMain main;

    void setLoginMain(LoginScreenMain main)
    {
        this.main = main;
    }

}

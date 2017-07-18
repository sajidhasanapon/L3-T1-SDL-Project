package app;/**
 * Created by apon on 7/9/17.
 */

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class LoginScreenMain extends Application
{
    public Stage window;

    @Override
    public void start(Stage primaryStage) throws Exception
    {
        window = primaryStage;

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("LoginScreenView.fxml"));
        Parent root = loader.load();

        LoginScreenController controller = loader.getController();
        controller.setLoginMain(this);

        primaryStage.setTitle("Sign In");
        primaryStage.setScene(new Scene(root, 400, 250));
        primaryStage.show();

    }

    public static void main(String[] args)
    {
        launch(args);
    }

}

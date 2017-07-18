package app;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class HomeScreenMain extends Application
{
    Stage window;
    String user;
    String pass;

    HomeScreenMain(Stage window, String user, String pass)
    {
        this.window = window;
        this.pass = pass;
        this.user = user;

        try
        {
            start(window);
        }
        catch (Exception e)
        {
            // ajaira
        }
    }

    @Override
    public void start(Stage window) throws Exception
    {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("HomeScreenView.fxml"));
        Parent root = loader.load();

        window.setTitle("Welcome");
        window.setScene(new Scene(root, 400, 300));
        window.show();

        HomeScreenController controller = loader.getController();
        controller.setThings(this, window, user, pass);
    }


    public void closeWindow()
    {
        window.close();
    }
}

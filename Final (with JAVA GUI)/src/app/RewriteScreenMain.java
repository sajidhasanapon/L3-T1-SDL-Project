package app;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class RewriteScreenMain extends Application
{
    Stage window;
    String fileName;
    HomeScreenMain main;


    //RewriteScreenMain(HomeScreenMain main, Stage window, String fileName)
    RewriteScreenMain(String fileName)
    {
        this.main = main;
        this.window = window;
        this.fileName = fileName;

        try
        {
            start(window);
            System.out.println("From rewritemain constructor");
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    @Override
    public void start(Stage window) throws Exception
    {
        window = new Stage();
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("RewriteScreenView.fxml"));
        Parent root = loader.load();

        window.setTitle("Edit");
        window.setScene(new Scene(root, 650, 600));
        window.show();

        RewriteScreenController controller = loader.getController();
        controller.setThings(this, window, fileName);
        System.out.println("From Rewritemain");
    }


}

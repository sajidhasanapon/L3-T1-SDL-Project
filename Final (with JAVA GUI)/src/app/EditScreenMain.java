package app;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class EditScreenMain extends Application
{
    String fileName;
    String filePath;

    EditScreenMain(String fileName, String filePath)
    {
        try
        {
            this.fileName = fileName;
            this.filePath = filePath;

            Stage window = new Stage();
            start(window);
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

    }

    @Override
    public void start(Stage window) throws Exception
    {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("EditScreenView.fxml"));
        Parent root = loader.load();

        EditScreenController controller = loader.getController();
        controller.setThings(fileName, filePath, window);

        window.setTitle("Edit Screen");
        window.setScene(new Scene(root, 1200, 750));
        window.show();
    }

}

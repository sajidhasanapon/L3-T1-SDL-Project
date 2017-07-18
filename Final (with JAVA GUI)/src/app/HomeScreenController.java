package app;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import javax.swing.*;
import java.io.*;
import java.nio.file.Files;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class HomeScreenController
{
    HomeScreenMain main;
    Stage window;
    String username;
    String password;

    public void setThings(HomeScreenMain main, Stage window, String username, String password)

    {
        this.main = main;
        this.window = window;
        this.username = username;
        this.password = password;
    }

    @FXML
    private StackPane mainPane;

    @FXML
    private Button newImageButton;

    @FXML
    private Button closeButton;

    @FXML
    private Button addNewUserButton;

    @FXML
    private Button editPreviousButton;

    @FXML
    void chooseNewImage(ActionEvent event) throws Exception
    {
        String imageName = "", imagePath = "";

        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Open Image");
        FileChooser.ExtensionFilter filter = new FileChooser.ExtensionFilter
                ("Image Files", "*.jpg", "*.png");
        fileChooser.getExtensionFilters().add(filter);

        Stage window = new Stage();
        File selectedImage;
        selectedImage = fileChooser.showOpenDialog(window);

        imageName = selectedImage.getName();
        imagePath = selectedImage.getAbsolutePath();


        Process p4 = Runtime.getRuntime().exec("./script.sh " + imagePath);
        InputStream in = p4.getInputStream();
        BufferedReader rd = new BufferedReader(new InputStreamReader(in));
        String line;
        while((line = rd.readLine()) != null)
        {
            System.out.println(line);
        }
        p4.waitFor();

        new EditScreenMain(imageName, imagePath);

        System.out.println("Selected = " + imagePath);
    }

    @FXML
    void closeApplication(ActionEvent event)
    {
        main.closeWindow();
    }

    @FXML
    void changePassword(ActionEvent event)
    {
        try
        {
            String newPass = "";
            while (newPass.equals(""))
            {
               newPass = JOptionPane.showInputDialog("Enter new password");
            }


            BufferedReader file = new BufferedReader(new FileReader("login"));
            String line;
            StringBuffer inputBuffer = new StringBuffer();
            while ((line = file.readLine()) != null) {
                inputBuffer.append(line);
                inputBuffer.append('\n');
            }
            String inputStr = inputBuffer.toString();
            file.close();

            inputStr = inputStr.replace(username+'\n'+password, username+'\n'+newPass);

            FileOutputStream fileOut = new FileOutputStream("login");
            fileOut.write(inputStr.getBytes());
            fileOut.close();

        }
        catch (Exception e)
        {

        }
    }

    @FXML
    public void addNewUser(ActionEvent event)
    {
        if(username.equals("admin") == false)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR, "Only admin can add a new user!");
            alert.showAndWait();

            return;
        }

        String newUser = JOptionPane.showInputDialog("Enter new username");
        String newPass = JOptionPane.showInputDialog("Enter new password for " + newUser);

        try
        {
            String filename= "login";
            FileWriter fw = new FileWriter(filename,true); //the true will append the new data
            fw.write(newUser+'\n'+newPass);//appends the string to the file
            fw.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

    }

    @FXML
    public void editPrevious(ActionEvent event)
    {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Open File");

        File userDirectory = new File("scanned/");
        fileChooser.setInitialDirectory(userDirectory);

        Stage window = new Stage();
        File selectedFile;
        selectedFile = fileChooser.showOpenDialog(window);

        String fileName = selectedFile.getName();
        //new RewriteScreenMain(main, window, fileName);
        new RewriteScreenMain(fileName);
        System.out.println("From HomeController");
        System.out.println(fileName);
    }


}

package app;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import javax.swing.*;
import java.io.*;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.ResourceBundle;

/**
 * Created by apon on 7/7/17.
 */
public class EditScreenController
{
    @FXML
    private AnchorPane editPane;

    @FXML
    private ImageView imageView;

    @FXML
    private Button testButton;

    @FXML
    private TextField nameBox;

    @FXML
    private TextField mobBox;

    @FXML
    private TextField dobBox;

    @FXML
    private TextField nidBox;

    @FXML
    private TextField mailBox;

    String filePath;
    String fileName;
    Stage window;

    BufferedReader br;
    BufferedWriter writer;

    String ROOT_DIRECTORY = System.getProperty("user.dir");
    String PY_CORE = ROOT_DIRECTORY + "/python/";


    public void setThings(String fileName, String filePath, Stage window)
    {
        this.filePath = filePath;
        this.fileName = fileName;
        this.window = window;

        System.out.println("From EditScreenController: " + filePath);
        System.out.println(System.getProperty("user.dir"));


        Image image = new Image("file:" + filePath);
        imageView.setImage(image);
        //imageView.setFitWidth(100);
        imageView.setPreserveRatio(true);


        try
        {
            final Font banglaFont = Font.loadFont(new FileInputStream(new File("fonts/kalpurush.ttf")), 20);

            nameBox.setFont(banglaFont);
            mobBox.setFont(banglaFont);
            dobBox.setFont(banglaFont);
            nidBox.setFont(banglaFont);
            mailBox.setFont(banglaFont);

            File inputFile = new File("python/output.txt");
            FileReader in = new FileReader(inputFile);
            br = new BufferedReader(in);

            nameBox.setText(br.readLine());
            mobBox.setText(br.readLine());
            dobBox.setText(br.readLine());
            nidBox.setText(br.readLine());
            mailBox.setText(br.readLine());

            br.close();
            inputFile.delete();

            //

            //

            //Process p1 = Runtime.getRuntime().exec("python " + PY_CORE + "rotate.py " + PY_CORE + "src.png");

            //System.out.println("Command = " + "python " + PY_CORE + "rotate.py " + PY_CORE + "src.png");

            //

            //Process p2 = Runtime.getRuntime().exec("python " + PY_CORE + "crop.py " + PY_CORE + "rotated.png");

            //System.out.println("Command = " + "python " + PY_CORE + "crop.py " + PY_CORE + "rotated.png");

            //

            //Process p3 = Runtime.getRuntime().exec("python " + PY_CORE + "sc.py");

            //System.out.println("Command = " + "python " + PY_CORE + "sc.py");

            //

            //Process p4 = Runtime.getRuntime().exec("python " + PY_CORE + "main.py");

            //System.out.println("Command = " + "python " + PY_CORE + "main.py");

            //

            //

            //Process p1 = Runtime.getRuntime().exec("python rotate.py src.png");
            //Process p2 = Runtime.getRuntime().exec("python crop.py rotated.png");
            //Process p3 = Runtime.getRuntime().exec("python sc.py");
            //Process p4 = Runtime.getRuntime().exec("python main.py");


            System.out.println("Completed");

        }
        catch (Exception e)
        {
            //TODO: who cares
        }
    }

    @FXML
    void saveImage(ActionEvent event)
    {
        String finalVal =   nameBox.getText() + '\n' +
                            mobBox.getText() + '\n' +
                            dobBox.getText() + '\n' +
                            nidBox.getText() + '\n' +
                            mailBox.getText() + '\n';
        try
        {
            String outPutFileName = fileName.substring(0, fileName.lastIndexOf(".")) + ".txt";
            FileWriter out = new FileWriter("scanned/" + outPutFileName);
            writer = new BufferedWriter(out);
            writer.write(finalVal);
            writer.close();

            window.close();
        }
        catch (Exception e)
        {
            //TODO: meow
        }
    }
}

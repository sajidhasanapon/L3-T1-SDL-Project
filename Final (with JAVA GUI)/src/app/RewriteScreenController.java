package app;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.awt.event.ActionEvent;
import java.io.*;

public class RewriteScreenController
{

    private RewriteScreenMain main;
    private Stage window;
    String fileName;

    @FXML
    private AnchorPane editPane;

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

    @FXML
    private Button saveButton;

    @FXML
    private Button backButton;

    public void setThings(RewriteScreenMain main, Stage window, String fileName)
    {
        this.main = main;
        this.window = window;
        this.fileName = fileName;

        show();
    }

    public void show()
    {
        try
        {
            final Font banglaFont = Font.loadFont(new FileInputStream(new File("fonts/kalpurush.ttf")), 20);

            nameBox.setFont(banglaFont);
            System.out.println(nameBox.getText());
            mobBox.setFont(banglaFont);
            dobBox.setFont(banglaFont);
            nidBox.setFont(banglaFont);
            mailBox.setFont(banglaFont);

            BufferedReader br = new BufferedReader(new FileReader("scanned/"+fileName));
            nameBox.setText(br.readLine());
            mobBox.setText(br.readLine());
            dobBox.setText(br.readLine());
            nidBox.setText(br.readLine());
            mailBox.setText(br.readLine());
        }
        catch (Exception e)
        {

        }
    }

    /*
    @FXML
    public void save(ActionEvent event)
    {
        String finalVal =   nameBox.getText() + '\n' +
                mobBox.getText() + '\n' +
                dobBox.getText() + '\n' +
                nidBox.getText() + '\n' +
                mailBox.getText() + '\n';

        try
        {
            BufferedWriter writer = null;
            FileWriter out = new FileWriter("scanned/" + fileName);
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
*/
}

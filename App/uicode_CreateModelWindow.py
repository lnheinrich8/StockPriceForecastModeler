from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QAbstractSpinBox,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QCheckBox,
    QListWidget
)

import json

from ui_form_createmodel import Ui_CreateModel
from uisource_DrawingWidget import DrawingWidget

class CreateModelWindow(QMainWindow):

    data_submitted = Signal(str)

    def __init__(self, column_names, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateModel()
        self.ui.setupUi(self)

        # column names from passed df in MainWindow
        self.column_names = column_names

        # right side params initialization

        self.ui.optimizer_combobox.addItems(["SGD", "RMSprop", "Adam","Adamw",
        "Adadelta", "Adagrad", "Adamax", "Nadam", "Ftrl", "Lion"])
        self.ui.optimizer_combobox.setCurrentText("Adam")

        self.ui.loss_combobox.addItems(["binary_crossentropy", "categorical_crossentropy",
        "sparse_categorical_crossentropy", "poisson", "ctc", "kl_divergence", "mean_squared_error",
        "mean_absolute_error", "mean_absolute_percentage_error", "mean_squared_logarithmic_error",
        "cosine_similarity", "huber", "log_cosh", "hinge", "squared_hinge", "categorical_hinge"])
        self.ui.loss_combobox.setCurrentText("mean_squared_error")

        self.ui.trainingcols_listwidget.addItems(self.column_names)
        self.ui.trainingcols_listwidget.setSelectionMode(QListWidget.MultiSelection)

        self.ui.target_combobox.addItems(self.column_names)


        self.updating_layers = False
        self.layer_count = 0
        self.checkbox_index = None
        self.dropout_val = None

        self.layer_widgets_dict = []  # store dictionaries for each layer
        self.layer_neuron_values = [] # store neuron values for each layer
        self.layer_type_values = [] # store type values for each layer
        self.layer_rseq_bools = [] # store rseq bools for each layer
        self.ui.layercount_spinBox.setValue(2)

        # Add the DrawingWidget
        self.drawing_widget = DrawingWidget()
        self.ui.drawing_layout = QVBoxLayout(self.ui.widget)
        self.ui.drawing_layout.addWidget(self.drawing_widget)

        # Initialize layer options container
        self.layer_options_container = QWidget()
        self.layer_options_layout = QVBoxLayout(self.layer_options_container)
        self.layer_options_container.setLayout(self.layer_options_layout)
        self.ui.layerCustomizationArea.setWidget(self.layer_options_container)
        self.ui.layerCustomizationArea.setWidgetResizable(True)

        # ---- CONNECT SIGNALS ----
        self.ui.layercount_spinBox.valueChanged.connect(self.layercount_spinbox_changed)
        self.ui.layercount_spinBox.valueChanged.connect(self.update_layer_options)

        # left side
        self.ui.clearrseq_button.clicked.connect(self.on_clearrseq_button_clicked)
        self.ui.restore_button.clicked.connect(self.on_restore_button_clicked)
        # right side
        self.ui.selectalltcols_button.clicked.connect(self.on_selectalltcols_button_clicked)
        self.ui.deselectalltcols_button.clicked.connect(self.on_deselectalltcols_button_clicked)

        # final signals
        self.ui.setmodel_button.clicked.connect(self.on_setmodel_button_clicked)

        # Initial drawing
        self.layercount_spinbox_changed(self.ui.layercount_spinBox.value())
        self.update_layer_options()

    # ---- SLOT FUNCTIONS ----

    # updates the layer drawing in the drawing widget
    def layercount_spinbox_changed(self, value):
        self.drawing_widget.draw_layers(value)

    def update_layer_options(self):
        # Re-create the layer options container and layout
        self.layer_options_container.deleteLater()
        self.layer_options_container = QWidget()  # Create a new container widget
        self.layer_options_layout = QVBoxLayout(self.layer_options_container)  # Create a new layout
        self.layer_options_container.setLayout(self.layer_options_layout)  # Set the new layout to the container
        self.ui.layerCustomizationArea.setWidget(self.layer_options_container)

        self.layer_options_layout.setAlignment(Qt.AlignTop)
        self.layer_widgets_dict.clear() # clear the layer widget dictionary

        # Add the horizontal layout for customization of each layer
        self.layer_count = self.ui.layercount_spinBox.value()
        for i in range(self.layer_count):
            layer_data = {}  # Dictionary to store widgets for this layer

            if i == self.layer_count - 1:
                layer_layout = QHBoxLayout()
                layer_label = QLabel("Output dropout %")
                layer_layout.addWidget(layer_label, alignment=Qt.AlignLeft)
                dropout_spinbox = QSpinBox(self)
                dropout_spinbox.setMinimum(1)
                dropout_spinbox.setMaximum(100)
                if self.dropout_val is None:
                    dropout_spinbox.setValue(20)  # Default value
                else:
                    dropout_spinbox.setValue(self.dropout_val)
                dropout_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
                layer_layout.addWidget(dropout_spinbox, alignment=Qt.AlignLeft)

                layer_data['dropout_spinbox'] = dropout_spinbox


            else:
                layer_layout = QHBoxLayout()

                # label for neurons
                layer_label = QLabel(f"L{i + 1}:")
                layer_layout.addWidget(layer_label, alignment=Qt.AlignLeft)
                # spinbox for neurons
                neuron_spinbox = QSpinBox(self)
                neuron_spinbox.setMinimum(1)  # Minimum number of neurons
                neuron_spinbox.setMaximum(500)  # Maximum number of neurons
                neuron_spinbox.setValue(32)  # Default value
                neuron_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
                layer_layout.addWidget(neuron_spinbox, alignment=Qt.AlignLeft)
                layer_data['neuron_spinbox'] = neuron_spinbox

                # label for type of layer
                type_label = QLabel("T:")
                layer_layout.addWidget(type_label, alignment=Qt.AlignLeft)
                # combobox for type of layer
                type_combobox = QComboBox(self)
                type_combobox.setFixedSize(70,20)
                type_combobox.addItems(["Dense", "LSTM", "GRU", "SimpleRNN"])  # Example types
                layer_layout.addWidget(type_combobox, alignment=Qt.AlignLeft)
                layer_data['type_combobox'] = type_combobox

                # label for return sequences
                rseq_label = QLabel("r_seq:")
                layer_layout.addWidget(rseq_label, alignment=Qt.AlignLeft)
                # checkbox for return sequences
                rseq_checkbox = QCheckBox(None)
                layer_layout.addWidget(rseq_checkbox, alignment=Qt.AlignLeft)
                layer_data['rseq_checkbox'] = rseq_checkbox

            # Add the horizontal layout to the main vertical layout
            self.layer_options_layout.addLayout(layer_layout)
            self.layer_widgets_dict.append(layer_data)

        # shitty way of doing this but whatever
        self.updating_layers = True
        self.update_neuron_spinboxes()
        self.update_type_comboboxes()
        self.update_rseq_checkboxes()
        self.updating_layers = False

        self.set_neuron_spinboxes_signals()
        self.set_type_comboboxes_signals()
        self.set_rseq_checkboxes_signals()
        self.set_dropout_spinbox_signal()


    # --- Neuron Shi ---
    def set_neuron_spinboxes_signals(self):
        for i, layer in enumerate(self.layer_widgets_dict):
            if i != len(self.layer_widgets_dict)-1:
                layer['neuron_spinbox'].valueChanged.connect(self.update_neuron_spinboxes)

                if i < len(self.layer_neuron_values):
                    self.layer_neuron_values[i] = layer['neuron_spinbox'].value()
                else:
                    self.layer_neuron_values.append(layer['neuron_spinbox'].value())
    def update_neuron_spinboxes(self):
        if self.updating_layers: # this is set to true when the layer count is changing
            for k in range(len(self.layer_neuron_values)):
                if k < self.layer_count-1:
                    self.layer_widgets_dict[k]['neuron_spinbox'].setValue(self.layer_neuron_values[k])
        else:
            for i, layer in enumerate(self.layer_widgets_dict):
                if i != len(self.layer_widgets_dict)-1:
                    self.layer_neuron_values[i] = layer['neuron_spinbox'].value()

    # --- Type Shi ---
    def set_type_comboboxes_signals(self):
        for i, layer in enumerate(self.layer_widgets_dict):
            if i != len(self.layer_widgets_dict)-1:
                layer['type_combobox'].currentIndexChanged.connect(self.update_type_comboboxes)
                layer['type_combobox'].currentIndexChanged.connect(self.update_rseq_checkboxes) # connect signal to updating rseq as well

                if i < len(self.layer_type_values):
                    self.layer_type_values[i] = layer['type_combobox'].currentIndex()
                else:
                    self.layer_type_values.append(layer['type_combobox'].currentIndex())
    def update_type_comboboxes(self):
        if self.updating_layers:
            for k in range(len(self.layer_type_values)):
                if k < self.layer_count-1:
                    self.layer_widgets_dict[k]['type_combobox'].setCurrentIndex(self.layer_type_values[k])
        else:
            for i, layer in enumerate(self.layer_widgets_dict):
                if i != len(self.layer_widgets_dict)-1:
                    self.layer_type_values[i] = layer['type_combobox'].currentIndex()

    # --- RSeq Shi ---
    def set_rseq_checkboxes_signals(self):
        for i, layer in enumerate(self.layer_widgets_dict):
            if i != len(self.layer_widgets_dict)-1:
                layer['rseq_checkbox'].stateChanged.connect(self.update_rseq_checkboxes)

                if i < len(self.layer_rseq_bools):
                    self.layer_rseq_bools[i] = layer['rseq_checkbox'].isChecked()
                else:
                    self.layer_rseq_bools.append(layer['rseq_checkbox'].isChecked())
    def update_rseq_checkboxes(self):
        if self.updating_layers:
            for k in range(len(self.layer_rseq_bools)):
                if k < self.layer_count-1:
                    if self.layer_widgets_dict[k]['type_combobox'].currentText() == 'Dense':
                        self.layer_widgets_dict[k]['rseq_checkbox'].setEnabled(False)
                    else:
                        self.layer_widgets_dict[k]['rseq_checkbox'].setChecked(self.layer_rseq_bools[k])
        else:
            for i, layer in enumerate(self.layer_widgets_dict):
                if i != len(self.layer_widgets_dict)-1:
                    if layer['type_combobox'].currentText() == 'Dense':
                        layer['rseq_checkbox'].setChecked(False)
                        layer['rseq_checkbox'].setEnabled(False)
                    else:
                        if i != len(self.layer_widgets_dict)-2 and self.layer_widgets_dict[i+1]['type_combobox'].currentText() in ['LSTM', 'GRU', 'SimpleRNN']:
                            layer['rseq_checkbox'].setChecked(True)
                            layer['rseq_checkbox'].setEnabled(False)
                            self.layer_rseq_bools[i] = layer['rseq_checkbox'].isChecked()
                        else:
                            layer['rseq_checkbox'].setEnabled(True)
                            self.layer_rseq_bools[i] = layer['rseq_checkbox'].isChecked()

    # --- Dropout Shi ---
    def set_dropout_spinbox_signal(self):
        dropout_spinbox = self.layer_widgets_dict[len(self.layer_widgets_dict)-1]['dropout_spinbox']
        dropout_spinbox.valueChanged.connect(self.update_dropout)
    def update_dropout(self):
        dropout_spinbox = self.layer_widgets_dict[len(self.layer_widgets_dict)-1]['dropout_spinbox']
        self.dropout_val = dropout_spinbox.value()


    def on_clearrseq_button_clicked(self):
        for i, layer in enumerate(self.layer_widgets_dict):
            if i != len(self.layer_widgets_dict)-1:
                layer['rseq_checkbox'].setChecked(False)
    def on_restore_button_clicked(self):
        self.layer_widgets_dict = []
        self.layer_neuron_values = []
        self.layer_type_values = []
        self.layer_rseq_bools = []
        self.dropout_val = 20
        self.on_clearrseq_button_clicked()
        self.update_layer_options()

    def on_selectalltcols_button_clicked(self):
        for row in range(self.ui.trainingcols_listwidget.count()):
            item = self.ui.trainingcols_listwidget.item(row)
            item.setSelected(True)
    def on_deselectalltcols_button_clicked(self):
        for row in range(self.ui.trainingcols_listwidget.count()):
            item = self.ui.trainingcols_listwidget.item(row)
            item.setSelected(False)

    def on_setmodel_button_clicked(self):
        # TODOOOOOOOOOOO additional data that needs to be serialized
        step_future = self.ui.stepfuture_spinbox.value()
        step_past = self.ui.steppast_spinbox.value()
        forecast_period = self.ui.forecastperiod_spinbox.value()
        epochs = self.ui.epochs_spinbox.value()
        optimizer = self.ui.optimizer_combobox.currentText()
        loss = self.ui.loss_combobox.currentText()
        target_variable = self.ui.target_combobox.currentText()
        trainingcols = []
        for row in range(self.ui.trainingcols_listwidget.count()):
            item = self.ui.trainingcols_listwidget.item(row)
            if item.isSelected():
                trainingcols.append(item.text())


        serialized_data = json.dumps([
            {key: widget.value() if isinstance(widget, QSpinBox) else widget.isChecked() if isinstance(widget, QCheckBox) else widget.currentText() for key, widget in layer.items()}
            for layer in self.layer_widgets_dict
        ])
        self.data_submitted.emit(serialized_data)
        self.close()


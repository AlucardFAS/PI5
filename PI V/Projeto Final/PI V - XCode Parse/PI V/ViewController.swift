//
//  ViewController.swift
//  PI V
//
//  Created by Danilo Mative on 03/03/2018.
//  Copyright © 2018 Danilo Mative. All rights reserved.
//

import Cocoa

class ViewController: NSViewController, NSMenuDelegate {

    //SETUP:
    var timer:Timer?
    var animationStage = 0
    var ignoreIndexes = [0]
    var normalizeIndexes:Array<Int> = []//,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    let archiveName = "myanimelist"
    let outputName = "myanimelist-output"
    
    @IBOutlet weak var predictButton: NSButton!
    @IBOutlet weak var animeNameTextField: NSTextField!
    @IBOutlet weak var graphView: GraphView!
    @IBOutlet weak var customGraphView: GraphView!
    @IBOutlet weak var producerButton: NSPopUpButton!
    @IBOutlet weak var studioButton: NSPopUpButton!
    @IBOutlet weak var sourceButton: NSPopUpButton!
    @IBOutlet weak var durationButton: NSPopUpButton!
    @IBOutlet weak var classificationButton: NSPopUpButton!
    @IBOutlet weak var episodesButton: NSPopUpButton!
    @IBOutlet weak var graphPopButton: NSPopUpButton!
    @IBOutlet weak var predictText: NSTextField!
    @IBOutlet weak var predictedScore: NSTextField!
    @IBOutlet weak var averageTExt: NSTextField!
    
    var activeSwitches = [Int]()
    
    var countMatrix = Array<Array<Int>>()
    var classesMatrix = Array<Array<String>>()
    var originalMatrix = Array<Array<String>>()
    var mainMatrix = Array<Array<String>>()
    
    let scoresList = [4.0,5.0,5.5,5.75,6.0,6.25,6.5,6.6,6.7,6.8,6.9,7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8.0,8.5,9.0]
    
    let producers = ["Bandai-Visual","TV-Tokyo","Aniplex","TV-Asahi","VAP","Kadokawa-Shoten","Starchild-Records","Fuji-TV","Lantis","Geneon-Universal-Entertainment","NHK","Sotsu","AIC","Genco","TBS","Pony-Canyon","Tokyo-Movie-Shinsha","KSS","Shogakukan-Productions","Outros"]
    
    let durations = ["0-a-5min","6-a-15min","16-a-26min","27-a-60min","1hr-ou-+","Desconhecido"]
    
    let episodes = ["1","2-a-6","7-a-13","14-a-26","27-a-52","53-a-100","100+","Desconhecido"]
    
    let studios = ["Kinema-Citrus","Bones","A-1-Pictures","Production-I.G","Kyoto-Animation","J.C.-Staff","Madhouse-Inc.","Wit-Studio","Aniplex","Shin-Ei-Animation","Xebec","DLE","Gonzo","Bandai-Visual","Sunrise","Manglobe","Studio-Deen","OLM","Tatsunoko-Production","Toei-Animation","Studio-Pierrot","Funimation","White-Fox","TNK","Lerche","AIC-Build","TMS-Entertainment","Nippon-Animation","Estudio-nao-listado"]
    
    let genres = ["Action","Adventure","Sci-Fi","Comedy","Drama","Romance","Fantasy","Mystery","School","Ecchi","SliceofLife","Mecha","Magic","Military","Sports","Historical","Horror","Supernatural","Shounen","Shoujo","Outro"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        /*
#colorLiteral(red: 0.9685536027, green: 0.9916532636, blue: 0.7745810151, alpha: 1)
         #colorLiteral(red: 0.9890047908, green: 0.9935602546, blue: 0.5933811665, alpha: 1)
         #colorLiteral(red: 0.4841502905, green: 0.6438478231, blue: 0.8267706037, alpha: 1)
        #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1) */
        
        self.graphPopButton.frame.size.height = 50.0
        self.graphPopButton.removeAllItems()
        self.graphPopButton.menu?.delegate = self
        
        self.graphPopButton.addItem(withTitle: "Distribuição de Produtores")
        self.graphPopButton.addItem(withTitle: "Distribuição de Estudios")
        self.graphPopButton.addItem(withTitle: "Distribuição de Durações de Episódios")
        self.graphPopButton.addItem(withTitle: "Distribuição de Número de Episódios")
        self.graphPopButton.addItem(withTitle: "Distribuição de Classificação")
        self.graphPopButton.addItem(withTitle: "Distribuição de Fontes")
        self.view.layer?.backgroundColor = #colorLiteral(red: 0.2543377578, green: 0.5782305002, blue: 0.7284123302, alpha: 1)
        predictButton.wantsLayer = true
        predictButton.layer?.backgroundColor = #colorLiteral(red: 0.4841502905, green: 0.6438478231, blue: 0.8267706037, alpha: 1)
        execute()
        loadValuesOnPopButtons()
       
        
        
        for view in self.view.subviews {
            
            if view.isKind(of: NSButton.self) {
                
                if let button = view as? NSButton {
                    
                    let color = #colorLiteral(red: 0.9890047908, green: 0.9935602546, blue: 0.5933811665, alpha: 1)
                    
                    if let mutableAttributedTitle = button.attributedTitle.mutableCopy() as? NSMutableAttributedString {
                        mutableAttributedTitle.addAttribute(.foregroundColor, value: color, range: NSRange(location: 0, length: mutableAttributedTitle.length))
                        button.attributedTitle = mutableAttributedTitle
                    }
                }
            }
            
        }
        
        // Do any additional setup after loading the view.
    }

    override func viewDidAppear() {
        super.viewDidAppear()
    }
    
    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
 
    func runScript(array:[Int]) {
        
        var arguments = ["/usr/local/Cellar/python/3.6.5/bin/useData.py"]
        arguments.append(String(array[0]))
        arguments.append(String(array[1]))
        arguments.append(String(array[2]))
        arguments.append(String(array[3]))
        arguments.append(String(array[4]))
        arguments.append(String(array[5]))

        let outPipe = Pipe()
        let errPipe = Pipe()
        
        let process = Process()
        process.launchPath =  "/usr/bin/python"
        process.arguments = arguments
        process.standardOutput = outPipe
        process.standardError = errPipe
        process.launch()
        
        let data = outPipe.fileHandleForReading.readDataToEndOfFile()
        let data2 = errPipe.fileHandleForReading.readDataToEndOfFile()
        
        //print(arguments)
        
        let exitCode = process.terminationStatus
        if (exitCode != 0) {
            print("ERROR: \(exitCode)")
            print(String(data: data2, encoding: String.Encoding.ascii) as Any)
            return
        }
        print(String(data: data, encoding: String.Encoding.ascii))
        let string = String(data: data, encoding: String.Encoding.ascii)
        let separate = string!.components(separatedBy: "\n")
        var number = separate[1].replacingOccurrences(of: "[", with: "")
        number = number.replacingOccurrences(of: "]", with: "")
        
        predictionReady(result:Int(number)!)
    }
    
    @IBAction func predictAction(_ sender: NSButton) {
        
        predictedScore.isHidden = true
        predictText.stringValue = "Prevendo Nota de \(self.animeNameTextField.stringValue)"
        predictText.isHidden = false
        
        
        if self.timer != nil {
            self.timer!.invalidate()
            self.timer = nil
        }
        
        self.timer = Timer.scheduledTimer(withTimeInterval: 0.6, repeats: true, block: { (Timer) in
            
            self.animationStage += 1
            
            var finaltext = ""
            
            if self.animationStage == 1 {
                finaltext = "."
            }
            else if self.animationStage == 2 {
                finaltext = ".."
            }
            else if self.animationStage == 3 {
                finaltext = "..."
            }
            else if self.animationStage == 4 {
                self.animationStage = 0
            }
            
            self.predictText.stringValue = "Prevendo Nota de \(self.animeNameTextField.stringValue)" + finaltext
        })
        
        //BACKGROUND THREAD
        
        runScript(array:[producerButton.index(of: producerButton.selectedItem!)+1,
                         studioButton.index(of: studioButton.selectedItem!)+1,
                         sourceButton.index(of: sourceButton.selectedItem!)+1,
                         durationButton.index(of: durationButton.selectedItem!)+1,
                         classificationButton.index(of: classificationButton.selectedItem!)+1,
                         episodesButton.index(of: episodesButton.selectedItem!)+1,])
        
    }
    
    func predictionReady(result:Int) {
        self.timer?.invalidate()
        self.timer = nil
        
        predictText.stringValue = "Nota esperada de \(self.animeNameTextField.stringValue):"
        predictedScore.stringValue = String(scoresList[result-1])
        predictedScore.isHidden = false
        
    }
    
    
    @IBAction func switchPressed(_ sender: NSButton) {
    
        if sender.state == .on {
            if activeSwitches.count < 3 {
                activeSwitches.append(sender.tag)
            }
            
            else {
                sender.state = .off
                print("No more than three genres can be selected!")
                //NO MORE THAN THREE GENRES!!!
            }
        }
        
        else if sender.state == .off {
            
            if let index = activeSwitches.index(of: sender.tag) {
                activeSwitches.remove(at: index)
            }
        }
        
    }
    
    func getValues(fromButton:NSPopUpButton)->[String] {
        
        var arr = [String]()
        
        let titles = fromButton.itemTitles
        
        for title in titles {
            arr.append(title.replacingOccurrences(of: " ", with: "-"))
        }
        
        return arr
    }
    
    func loadValuesOnPopButtons() {
        
        setPopUpItems(button: self.episodesButton, items: episodes)
        setPopUpItems(button: self.producerButton, items: producers)
        setPopUpItems(button: self.durationButton, items: durations)
        setPopUpItems(button: studioButton, items: studios)
        
        var ratings = classesMatrix[9]
        
        for i in 0..<ratings.count {
            ratings[i] = ratings[i].replacingOccurrences(of: "-", with: "")
        }
        
        setPopUpItems(button: classificationButton, items: ratings)

        var sources = classesMatrix[4]
        
        for i in 0..<sources.count {
            sources[i] = sources[i].replacingOccurrences(of: "-", with: "")
        }
        
        setPopUpItems(button: sourceButton, items: sources)
    }
    
    func setPopUpItems(button:NSPopUpButton, items:[String]) {
        
        adjustButton(button: button)
        
        button.removeAllItems()
        
        for item in items {
            
            let text = item.replacingOccurrences(of: "-", with: " ")
            button.addItem(withTitle: text)
        }
    }
    
    func adjustButton(button:NSPopUpButton) {
        
        button.frame.size.height = 45.0
        
    }
    
    func menuDidClose(_ menu: NSMenu) {
        
        if graphPopButton.selectedItem == nil {
            return
        }
        
        else {
            drawGraphicsWithTitle(title: graphPopButton.selectedItem!.title)
        }
    }
    
    func menu(_ menu: NSMenu, willHighlight item: NSMenuItem?) {
        
        if item == nil {
            return
        }
            
        else {
            drawGraphicsWithTitle(title: item!.title)
        }
    }
    
    func drawGraphicsWithTitle(title:String) {
        if (title.contains("Produtores")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:2, organizedData: producers)
        }
            
        else if (title.contains("Estudios")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:3, organizedData: studios)
        }
            
        else if (title.contains("Durações")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:8, organizedData: durations)
        }
            
        else if (title.contains("Número")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:10, organizedData: episodes)
        }
            
        else if (title.contains("Fontes")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:4, organizedData: classesMatrix[4])
        }
            
        else if (title.contains("Classificação")) {
            customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:9, organizedData: classesMatrix[9])
        }
        
        customGraphView.needsDisplay = true
    }
    
    func execute() {
        
        //path for file Fila
        let path = Bundle.main.path(forResource: archiveName, ofType: "txt")
        
        //pass the file to string
        let fullStr = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
        
        //let separator : Character = ","

        //Split the sting in array of strings separated by \n
        let lineArray = fullStr.components(separatedBy: "\n")
        
        //let normalizeIndexes = [0,1,2,3]
        
        for _ in 0..<40 {
            classesMatrix.append(Array<String>())
            countMatrix.append(Array<Int>())
        }
        
        for x in 0..<lineArray.count-1 {
         
            var correctColumns = Array<String>()
            let columns = lineArray[x].components(separatedBy: ",")
            
            var copyArray = Array<String>()
            for column in columns {
                copyArray.append(column.replacingOccurrences(of: " ", with: ""))
            }
            originalMatrix.append(copyArray)
            
            //Removes null data
            var isNull = false
            
            for y in 0..<columns.count {
                
                var object = columns[y]
                
                if object.contains("?") {
                    isNull = true
                    
                    break
                }
                
                //MARK:SCORE
                // ========== [ SCORE ]  ========== //
                if y == 11 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    
                    if let score = Double(object) {
                        
                        var text = ""
                        
                        if score <= 4.0 {
                            text = "Less-than-4.0"
                            object = String(1)
                        }
                        else if score <= 5.25 {
                            text = "Aprox-5.0"
                            object = String(2)
                        }
                        else if score <= 5.625 {
                            text = "Aprox-5.5"
                            object = String(3)
                        }
                        else if score <= 5.875 {
                            text = "Aprox-5.75"
                            object = String(4)
                        }
                        else if score <= 6.125 {
                            text = "Aprox-6.0"
                            object = String(5)
                        }
                        else if score <= 6.375 {
                            text = "Aprox-6.25"
                            object = String(6)
                        }else if score <= 6.55 {
                            text = "Aprox-6.5"
                            object = String(7)
                        }
                        else if score <= 6.65 {
                            text = "Aprox-6.6"
                            object = String(8)
                        }
                        else if score <= 6.75 {
                            text = "Aprox-6.7"
                            object = String(9)
                        }
                        else if score <= 6.85 {
                            text = "Aprox-6.8"
                            object = String(10)
                        }
                        else if score <= 6.95 {
                            text = "Aprox-6.9"
                            object = String(11)
                        }
                        else if score <= 7.05 {
                            text = "Aprox-7.0"
                            object = String(12)
                        }
                        else if score <= 7.15 {
                            text = "Aprox-7.1"
                            object = String(13)
                        }
                        else if score <= 7.25 {
                            text = "Aprox-7.2"
                            object = String(14)
                        }
                        else if score <= 7.35 {
                            text = "Aprox-7.3"
                            object = String(15)
                        }
                        else if score <= 7.45 {
                            text = "Aprox-7.4"
                            object = String(16)
                        }
                        else if score <= 7.55 {
                            text = "Aprox-7.5"
                            object = String(17)
                        }
                        else if score <= 7.65 {
                            text = "Aprox-7.6"
                            object = String(18)
                        }
                        else if score <= 7.75 {
                            text = "Aprox-7.7"
                            object = String(19)
                        }
                        else if score <= 7.85 {
                            text = "Aprox-7.8"
                            object = String(20)
                        }
                        else if score <= 7.95 {
                            text = "Aprox-7.9"
                            object = String(21)
                        }
                        else if score <= 8.25 {
                            text = "Aprox-8.0"
                            object = String(22)
                        }
                        else if score <= 8.75 {
                            text = "Aprox-8.5"
                            object = String(23)
                        }
                        else {
                            text = "Aprox-9.0"
                            object = String(24)
                        }
                        
                        if classesMatrix[y].index(of: text) == nil {
                            
                            classesMatrix[y].append(text)
                            countMatrix[y].append(1)
                        }
                            
                        else {
                            
                            let ind = classesMatrix[y].index(of: text)!
                            countMatrix[y][ind] = countMatrix[y][ind] + 1
                        }
                        
                        
                    }
                    
                }
                
                    //MARK:GENRES
                    // ========== [ GENRES ]  ========== //
                else if y == 5 || y == 6 || y == 7 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    var text = ""
                    
                    if let index = genres.index(of: object) {
                        text = object
                        object = String(index+1)
                    }
                    else {
                        text = "Outro"
                        object = String(22)
                    }
                    
                    if !text.contains("invalid") {
                        for value in 5...7 {
                            
                            if classesMatrix[value].index(of: text) == nil {
                                
                                classesMatrix[value].append(text)
                                countMatrix[value].append(1)
                            }
                                
                            else {
                                
                                let ind = classesMatrix[value].index(of: text)!
                                countMatrix[value][ind] = countMatrix[value][ind] + 1
                            }
                            
                        }
                    }
                }
                    
                    //MARK:EPISODE COUNT
// ========== [ EPISODE COUNT ]  ========== //
                else if y == 10 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    
                    if let ep = Int(object) {
                        
                        var text = ""
                        
                        if ep <= 0 {
                            object = String(8)
                            text = self.episodes[7]
                        }
                        else if ep <= 1 {
                            object = String(1)
                            text = self.episodes[0]
                        }
                        else if ep <= 6 {
                            object = String(2)
                            text = self.episodes[1]
                        }
                        else if ep <= 13 {
                            object = String(3)
                            text = self.episodes[2]
                        }
                        else if ep <= 26 {
                            object = String(4)
                            text = self.episodes[3]
                        }
                        else if ep <= 52 {
                            object = String(5)
                            text = self.episodes[4]
                        }
                        else if ep <= 100 {
                            object = String(6)
                            text = self.episodes[5]
                        }
                        else {
                            object = String(7)
                            text = self.episodes[6]
                        }
                        
                        if classesMatrix[y].index(of: text) == nil {
                            
                            classesMatrix[y].append(text)
                            countMatrix[y].append(1)
                        }
                            
                        else {
                            
                            let ind = classesMatrix[y].index(of: text)!
                            countMatrix[y][ind] = countMatrix[y][ind] + 1
                        }
                    }
                    
                }
                    //MARK:EPISODE DURATION
// ========== [ EPISODE TIME ]  ========== //
               
                else if y == 8 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    
                    var totalMinutes = 0
                    
                    if object.contains("hr") {
                        
                        object = object.replacingOccurrences(of: "hr", with: "x")
                        let twoValues = object.split(separator: "x")
                        var leftValue = String(twoValues.first!)
                        leftValue = leftValue.replacingOccurrences(of: "-", with: "")
                        leftValue = leftValue.replacingOccurrences(of: ".", with: "")
                        leftValue = leftValue.trimmingCharacters(in: .letters)
                        
                        if let hours = Int(leftValue) {
                            
                            totalMinutes = (hours * 60)
                            object = String(twoValues.last!)
                        }
                    }
                    
                    if object.contains("min") {
                        
                        object = object.replacingOccurrences(of: "min", with: "x")
                        let twoValues = object.split(separator: "x")
                        
                        var leftValue = String(twoValues.first!)
                        leftValue = leftValue.replacingOccurrences(of: "-", with: "")
                        leftValue = leftValue.replacingOccurrences(of: ".", with: "")
                        leftValue = leftValue.trimmingCharacters(in: .letters)
                        
                        if let minutes = Int(leftValue) {
                            
                            totalMinutes = totalMinutes + minutes
                        }
                    }
                    
                    var text = "Time"
                    
                    if totalMinutes <= 5 {
                        object = String(1)
                        text = self.durations[0]
                    }
                    else if totalMinutes <= 15 {
                        object = String(2)
                        text = self.durations[1]
                    }
                    else if totalMinutes <= 26 {
                        object = String(3)
                        text = self.durations[2]
                    }
                    else if totalMinutes <= 60 {
                        object = String(4)
                        text = self.durations[3]
                    }
                    else if totalMinutes > 60 {
                        object = String(5)
                        text = self.durations[4]
                    }
                    else {
                        object = String(6)
                        text = self.durations[5]
                    }
                    
                    if classesMatrix[y].index(of: text) == nil {
                        
                        classesMatrix[y].append(text)
                        countMatrix[y].append(1)
                    }
                        
                    else {
                        
                        let ind = classesMatrix[y].index(of: text)!
                        countMatrix[y][ind] = countMatrix[y][ind] + 1
                    }
                }
                
                    //MARK:STUDIOS
                    // ========== [ STUDIOS ]  ========== //
                else if y == 3 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    var text = object
                    
                    if let index = studios.index(of: object) {
                        object = String(index+1)
                    }
                    else {
                        text = studios.last!
                    }
                    
                    if classesMatrix[y].index(of: text) == nil {
                        
                        classesMatrix[y].append(text)
                        countMatrix[y].append(1)
                    }
                        
                    else {
                        
                        let ind = classesMatrix[y].index(of: text)!
                        countMatrix[y][ind] = countMatrix[y][ind] + 1
                    }
                    
                }
                    
                    //MARK:PRODUCERS
// ========== [ PRODUCERS ]  ========== //
                else if y == 2 {
                    
                    object = object.replacingOccurrences(of: " ", with: "")
                    var text = object
                    
                    
                    if let index = producers.index(of: object) {
                        object = String(Int(index))
                    }
                    else {
                        text = "Outros"
                        object = String(20)
                    }
                    
                    
                    if classesMatrix[y].index(of: text) == nil {
                        
                        classesMatrix[y].append(text)
                        countMatrix[y].append(1)
                    }
                        
                    else {
                        
                        let ind = classesMatrix[y].index(of: text)!
                        countMatrix[y][ind] = countMatrix[y][ind] + 1
                    }
                    

                }
                
                    
                else if normalizeIndexes.index(of: y) == nil && ignoreIndexes.index(of: y) == nil {
                    
                    if classesMatrix[y].index(of: object) == nil {
                        
                        classesMatrix[y].append(object)
                        countMatrix[y].append(1)
                        object = String(classesMatrix[y].count)
                    }
                    
                    else {
                        
                        let ind = classesMatrix[y].index(of: object)!
                        
                        countMatrix[y][ind] = countMatrix[y][ind] + 1
                        object = String(ind + 1)
                    }
                }
                
                correctColumns.append(object.replacingOccurrences(of: " ", with: ""))
            }
            
            if !isNull {
                mainMatrix.append(correctColumns)
            }

        }

        //MARK:GraphView
        // ========== [ GRAPH ]  ========== //
        
        var valArray = Array<Double>()
        
        for arr in originalMatrix {
            valArray.append(Double(arr.last!)!)
        }
        
        graphView.drawWithValues(values: valArray)
        
        customGraphView.drawWithClassesAndCounts(classMatrix: classesMatrix, countMatrix: countMatrix, row:2, organizedData: producers)
        
        var minArray = Array<Double>()
        var maxArray = Array<Double>()
        
        for _ in normalizeIndexes {
            minArray.append(999999.99)
            maxArray.append(0.0)
        }
        
        //Outliers
        for i in 0..<normalizeIndexes.count {
            
            generateOutliersForIndex(index: normalizeIndexes[i])
        }
        
        //Get max/min for each
        for x in 0..<mainMatrix.count {
            
            var line = mainMatrix[x]
            
            for i in 0..<normalizeIndexes.count {
                
                var str = line[ normalizeIndexes[i] ]
                
                if line[ normalizeIndexes[i] ].contains("x") {
                    str = line[ normalizeIndexes[i] ].replacingOccurrences(of: "x", with: "")
                }
                
                if let value = Double(str) {
                   
                    if value > maxArray[i] {
                        maxArray[i] = value
                    }
                    
                    if value < minArray[i] {
                        minArray[i] = value
                    }
                    
                }
                
                else {
                    print("ISSUES")
                }
            }
        }
        
        print(minArray)
        print(maxArray)
        
        
        for x in 0..<mainMatrix.count {
            
            var line = mainMatrix[x]
            
            for i in 0..<normalizeIndexes.count {
                
                var str = line[ normalizeIndexes[i] ]
                
                var isOutlier = false
                
                if line[ normalizeIndexes[i] ].contains("x") {
                    str = line[ normalizeIndexes[i] ].replacingOccurrences(of: "x", with: "")
                    isOutlier = true
                }
                
                if let value = Double(str) {
                    
                    let newValue:Double = Double(value - minArray[i]) / Double(maxArray[i] - minArray[i])
                    
//                    if newValue > 1.0 {
//                        print("QQQQQQ")
//                    }
                    
                    if isOutlier {
                        mainMatrix[x][ normalizeIndexes[i] ] = "x" + String(format: "%.2f", newValue)
                    }
                    
                    else {
                        mainMatrix[x][ normalizeIndexes[i] ] = String(format: "%.2f", newValue)
                    }
                    
                }
                
                else {
                    print("ISSUES")
                }
            }
        }

        
        var finalString = String()
        
        for x in 0..<mainMatrix.count {
            
            let line = mainMatrix[x]
            
            for object in line {
                
                finalString.append(object)
                finalString.append(",")
            }
            
            finalString.removeLast()
            finalString.append("\n")
        }
        
        finalString.append("\n")
    
    
        
        let filepath = getDocumentsDirectory().appendingPathComponent(outputName + ".txt")

        
        do {
            //try finalString.write(toFile: filepath, atomically: false, encoding: String.Encoding.utf8)
            try finalString.write(to: filepath, atomically: true, encoding: String.Encoding.utf8)
            
        } catch {
            print("EPAAA \(error)")
        }

        
        
        for x in 11...11 { //0..<classesMatrix.count {
            
            if normalizeIndexes.index(of: x) == nil && ignoreIndexes.index(of: x) == nil {
                
                print("==================================")
                
                var organizeVector = Array<Int>()
                
                for y in 0..<classesMatrix[x].count {
                    
                    organizeVector.append(countMatrix[x][y])
                    
                    print("Class " + classesMatrix[x][y] + " has " + String(countMatrix[x][y]))
    
                }

                //print(organizeVector.sorted())
            }
        }
                
        
        print("FINISHED!")
        
    }
    
    
    func generateOutliersForIndex(index:Int) {
        
        var orderArray = Array<Double>()
        
        for i in 0..<mainMatrix.count {
            
            let line = mainMatrix[i]
            orderArray.append(Double(line[index])!)
        }
        
        orderArray.sort()
        
        
        //var average = 0.0
        var q1 = 0.0
        var q3 = 0.0
        let idx : Int = orderArray.count / 2
        let value = orderArray[idx]
        var new = 0.0
        
        for i in idx+1..<orderArray.count {
            
            new = orderArray[i]
            
            if new > value {
                //average = (value - new) / 2.0
                break
            }
        }
        
        q1 = (orderArray[idx / 2] + value) / 2.0
        q3 = (orderArray[idx + (idx / 2)] + new) / 2.0
        
        let distance = (q3 - q1) * 1.5
        
        let upperRange = q3 + distance
        let lowerRange = q1 - distance
        
        for i in 0..<mainMatrix.count {
            
            let line = mainMatrix[i]
            
            if let value = Double(line[index]) {
                
                if value < lowerRange {
                    mainMatrix[i][index] = "x" + String(format: "%.2f", value)
                }
                
                else if value > upperRange {
                    mainMatrix[i][index] = "x" + String(format: "%.2f", value)
                }
                
                if value < 0 {
                    print("WHAAAAAA?")
                }
                
            }
        }
        
    }
    
    
    func getDocumentsDirectory() -> URL {
        let paths = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)
        return paths[0]
    }
    
    

}


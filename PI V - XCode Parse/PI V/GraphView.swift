//
//  GraphView.swift
//  PI V
//
//  Created by Danilo Mative on 05/06/2018.
//  Copyright © 2018 Danilo Mative. All rights reserved.
//

import Cocoa

class GraphView: NSView {

    var textValues = [String]()
    
    var countArray = Array<Int>()
    var max = 0
    
    let styles = ["bar","line"]
    let style = "bar"
    let maxValue = 9.5
    let iteration = 1.0
    let minValue = 2.0
    
    var drawWithValues = true
    var topText:NSTextField?
    
    func drawWithClassesAndCounts(classMatrix:[[String]],countMatrix:[[Int]], row:Int, organizedData:[String]) {
        
        //print(countMatrix)
        
        topText?.stringValue = ""
        textValues = [String]()
        
        countArray = Array<Int>()
        drawWithValues = false
        max = 0
        
        var allData = organizedData
        
        allData.removeLast()
        
        for data in allData {
            
            if let index = classMatrix[row].index(of: data) {
                
                countArray.append(countMatrix[row][index])
            }
            
            else {
                countArray.append(0)
            }
        }
        
        for x in countArray {
            if x > max {
                max = x
            }
        }
        
        textValues = allData
    }
    
    func drawWithValues(values:Array<Double>) {
        
        topText?.stringValue = ""
        textValues = [String]()
        
        countArray = Array<Int>()
        drawWithValues = true
        max = 0
        
        var current = minValue
        var c = 1
        
        while current <= maxValue {
            
            var count = 0
            
            for num in values {

                if num > current - (iteration/2.0) && num < current + (iteration/2.0) {
                    count = count + 1
                }
            }
            
            countArray.append(count)
            
            if c >= 1 {
                let text = NSText()
                text.alignment = .left
                text.backgroundColor = NSColor.clear
                text.string = String(format:"%.1f", current)
                text.font = NSFont(name: "Avenir", size: 11.0)
                text.isEditable = false
                text.textColor = #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1)
                text.frame.size = NSSize(width: 45.0, height: 4.0)
                text.frame.origin.y = CGFloat(self.frame.size.height - 17.0)
                text.frame.origin.x = CGFloat(((current - minValue) / (maxValue - minValue + (iteration/2.0))) * Double(self.frame.size.width))
                text.frame.origin.x += 10.0
                
                self.addSubview(text)
                c = 1
            }
            else {
                c += 1
            }
            textValues.append(String(format:"%.1f", current))
            current += iteration
        }
        
        for x in countArray {
            if x > max {
                max = x + Int(Double(x) * 0.1)
            }
        }
        

    }
    
    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)
        
        #colorLiteral(red: 0.9685536027, green: 0.9916532636, blue: 0.7745810151, alpha: 1).set()
        let backPath = NSBezierPath(rect:self.bounds)
        backPath.fill()
        
        let yIncrease = (self.frame.size.height - 40.0) / CGFloat(max)
        let xIncrease = self.frame.size.width / CGFloat(countArray.count)
        
        for x in 0..<countArray.count {
            
            if self.style == "line" {
                
                #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1).set()
                
                let path = NSBezierPath(rect: NSRect(x: CGFloat(x) * xIncrease + 10.0, y: 0.0, width: 2.0, height: self.frame.size.height * 0.97))
                path.fill()
                
                #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1).set()
                
                let size = 6.0
                let path2 = NSBezierPath(roundedRect: NSRect(x: (CGFloat(x) * xIncrease) - CGFloat(size) + 10.0, y: (CGFloat(countArray[x]) * yIncrease) - CGFloat(size), width: CGFloat(size*2.0), height: CGFloat(size*2.0)), xRadius: CGFloat(size), yRadius: CGFloat(size))
                path2.fill()
            }
            
            else if self.style == "bar" {
                
               #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1).set()
                let path = NSBezierPath(rect: NSRect(x: CGFloat(x) * xIncrease, y: 0.0, width: xIncrease - 2.0, height: CGFloat(countArray[x]) * yIncrease))
                path.fill()
                
            }
        }
    }
    
    override func mouseDown(with event: NSEvent) {
        
        let value = self.frame.size.width / CGFloat(countArray.count)
        
        let posXGraph = event.locationInWindow.x - self.frame.origin.x
        
        showDataTitle(index: Int(posXGraph / value))
    }
    
    func showDataTitle(index:Int) {
        
        if topText == nil {
            
            topText = NSTextField(frame: NSRect(x: 0.0, y: self.frame.size.height - 38.0, width: self.frame.size.width, height: 30.0))
            topText?.textColor =   #colorLiteral(red: 0.3830797076, green: 0.2501659691, blue: 0.2571684122, alpha: 1)
            topText?.font = NSFont(name: "Avenir-Medium", size: 18.0)
            topText?.alignment = .center
            topText?.backgroundColor = .clear
            topText?.isBordered = false
            topText?.isEditable = false
            self.addSubview(topText!)
            
        }
        
        if index < textValues.count {
            topText?.stringValue = textValues[index] + " (\(countArray[index]))"
        }
    }

}

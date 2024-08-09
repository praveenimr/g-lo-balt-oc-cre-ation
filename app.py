import streamlit as st
import pandas as pd
import xlrd
from io import StringIO

def part1(keyword):
    ch1 = ("<strong>Chapter 1: Introduction</strong>\n\t1.1 Research Objectives\n\t1.2 Research Methodology\n\t1.3 Research Process"
           +"\n\t1.4 Scope and Coverage\n\t\t1.4.1 Market Definition\n\t\t1.4.2 Key Questions Answered\n\t1.5 Market Segmentation"
           +"\n\n<strong>Chapter 2:Executive Summary</strong>")
    return ch1.replace("\n","<br />").replace("\t","&emsp;")

def part1B(keyword):
    ch1 = ("\n\n<strong>Chapter 4: Market Landscape</strong>\n\t4.1 Porter's Five Forces Analysis"
          +"\n\t\t4.1.1 Bargaining Power of Supplier\n\t\t4.1.2 Threat of New Entrants"
          +"\n\t\t4.1.3 Threat of Substitutes\n\t\t4.1.4 Competitive Rivalry\n\t\t4.1.5 Bargaining Power Among Buyers"
          +"\n\t4.2 Industry Value Chain Analysis\n\t4.3 Market Dynamics\n\t\t4.3.1 Drivers\n\t\t4.3.2 Restraints\n\t\t4.3.3 Opportunities"
          +"\n\t\t4.5.4 Challenges\n\t4.4 Pestle Analysis\n\t4.5 Technological Roadmap\n\t4.6 Regulatory Landscape\n\t4.7 SWOT Analysis"
          +"\n\t4.8 Price Trend Analysis\n\t4.9 Patent Analysis\n\t4.10 Analysis of the Impact of Covid-19\n\t\t4.10.1 Impact on the Overall Market\n\t\t4.10.2 Impact on the Supply Chain"
          +"\n\t\t4.10.3 Impact on the Key Manufacturers\n\t\t4.10.4 Impact on the Pricing")
    return ch1.replace("\n","<br />").replace("\t","&emsp;")

def part2(keyword, segmentation):
    count = 5
    segment = segmentation.split("#")
    ch2 = ""
    segment_heading = []
    for s in segment:
        x = s.split("::")
        segment_heading.append(x[0])
        ch2 += ("\n\n<strong>Chapter "+str(count)+": "+str(keyword)+" Market by "+x[0]+"</strong>\n\t"+str(count)+".1 "+str(keyword)+" Market Overview Snapshot and Growth Engine\n\t"+str(count)+".2 "+str(keyword)+" Market Overview")
        y = x[1].split(",")
        counter = 3
        for types in y:
            ch2 += ("\n\t"+str(count)+"."+str(counter)+" "+str(types)+"\n\t\t"+str(count)+"."+str(counter)+".1 Introduction and Market Overview\n\t\t"
                    +str(count)+"."+str(counter)+".2 Historic and Forecasted Market Size (2016-2030F)\n\t\t"
                    +str(count)+"."+str(counter)+".3 Key Market Trends, Growth Factors and Opportunities\n\t\t"
                    +str(count)+"."+str(counter)+".4 "+str(types)+": Geographic Segmentation")
            counter += 1
        count += 1
    return ch2.replace("\n","<br />").replace("\t","&emsp;"), segment_heading, count

def part3A(keyword, segmentation_heading):
    ch4 = "\n\n<strong>Chapter 3:Growth Opportunities By Segment</strong>"
    counter = 1
    for x in segmentation_heading:
        ch4 = ch4 + "\n\t3."+str(counter)+" By "+x.strip()
        counter += 1
    return ch4.replace("\n","<br />").replace("\t","&emsp;")

def part3(keyword, players, count):
    t = players.split(",")
    ch3 = ("\n\n<strong>Chapter "+str(count)+": Company Profiles and Competitive Analysis</strong>\n\t"+str(count)+".1 Competitive Landscape\n\t\t"
            +str(count)+".1.1 Competitive Positioning\n\t\t"
            +str(count)+".1.2 "+str(keyword)+" Sales and Market Share By Players\n\t\t"
            +str(count)+".1.3 Industry BCG Matrix\n\t\t"
            +str(count)+".1.4 Heat Map Analysis\n\t\t"
            +str(count)+".1.5 "+str(keyword)+" Industry Concentration Ratio (CR5 and HHI)\n\t\t"
            +str(count)+".1.6 Top 5 "+str(keyword)+" Players Market Share\n\t\t"
            +str(count)+".1.7 Mergers and Acquisitions\n\t\t"
            +str(count)+".1.8 Business Strategies By Top Players")
    counter = 2
    for i in t:
        if counter == 2:
            ch3 = ch3 + ("\n\t"+str(count)+"."+str(counter)+" "+i.strip().upper()
                     +"\n\t\t"+str(count)+"."+str(counter)+".1 Company Overview"
                     +"\n\t\t"+str(count)+"."+str(counter)+".2 Key Executives"
                     +"\n\t\t"+str(count)+"."+str(counter)+".3 Company Snapshot"
                     +"\n\t\t"+str(count)+"."+str(counter)+".4 Operating Business Segments"
                     +"\n\t\t"+str(count)+"."+str(counter)+".5 Product Portfolio"
                     +"\n\t\t"+str(count)+"."+str(counter)+".6 Business Performance"
                     +"\n\t\t"+str(count)+"."+str(counter)+".7 Key Strategic Moves and Recent Developments"
                     +"\n\t\t"+str(count)+"."+str(counter)+".8 SWOT Analysis")
        else:
            ch3 = ch3 + ("\n\t"+str(count)+"."+str(counter)+" "+i.strip().upper())
        counter += 1
    return ch3.replace("\n","<br />").replace("\t","&emsp;"), count

def part4(keyword, regions, count, segmentation):
    segment = segmentation.split("#")
    ch4 = "\n\n<strong>Chapter "+str(count)+": Global "+str(keyword)+" Market Analysis, Insights and Forecast, 2016-2030</strong>\n\t"+str(count)+".1 Market Overview"
    counter = 2
    for s in segment:
        x = s.split("::")
        ch4 = ch4 + "\n\t"+str(count)+"."+str(counter)+" Historic and Forecasted Market Size By "+x[0]
        y = x[1].split(",")
        for idx, z in enumerate(y):
            ch4 = ch4 + "\n\t\t"+str(count)+"."+str(counter)+"."+str(idx+1)+" "+str(z)
        counter += 1
    return ch4.replace("\n","<br />").replace("\t","&emsp;"), count

def part5(keyword, regions, count, segmentation):
    t = regions.split(",")
    segment = segmentation.split("#")
    ch4 = ""
    for i in t:
        counter = 1
        region = i.split("(")
        ch4 = ch4 + "\n\n<strong>Chapter "+str(count)+": "+region[0].strip()+" "+str(keyword)+" Market Analysis, Insights and Forecast, 2016-2030</strong>"
        ch4 = ch4 + ("\n\t"+str(count)+"."+str(counter)+" Key Market Trends, Growth Factors and Opportunities"
                     +"\n\t"+str(count)+"."+str(counter+1)+" Impact of Covid-19"
                     +"\n\t"+str(count)+"."+str(counter+2)+" Key Players"
                     +"\n\t"+str(count)+"."+str(counter+3)+" Key Market Trends, Growth Factors and Opportunities")
        segment_counter = 4
        for s in segment:
            x = s.split("::")
            ch4 = ch4 + "\n\t"+str(count)+"."+str(segment_counter)+" Historic and Forecasted Market Size By "+x[0]
            y = x[1].split(",")
            for idx, z in enumerate(y):
                ch4 = ch4 + "\n\t\t"+str(count)+"."+str(segment_counter)+"."+str(idx+1)+" "+str(z)
            segment_counter += 1
        region[1] = region[1].replace(")","")
        ch4 = ch4 +"\n\t"+str(count)+"."+str(segment_counter)+" Historic and Forecast Market Size by Country"
        for idx, country in enumerate(region[1].split(",")[0].split(";")):
            ch4 = ch4 +"\n\t\t"+str(count)+"."+str(segment_counter)+"."+str(idx+1)+" "+country.strip()
        counter += 1
        count += 1
    return ch4.replace("\n","<br />").replace("\t","&emsp;"), count

def part6(keyword, count):
    ch4 = "\n\n<strong>Chapter "+str(count)+" Investment Analysis</strong>\n\t"+str(count)+".1 Investment Trends"
    return ch4.replace("\n","<br />").replace("\t","&emsp;")

def table(keyword, segmentation, regions, players):
    return f"""
    <table>
        <thead>
            <tr>
                <th colspan="2">Table of Contents</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Introduction</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Market Landscape</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Growth Opportunities By Segment</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Company Profiles and Competitive Analysis</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Global Market Analysis, Insights and Forecast</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Regional Market Analysis</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Investment Analysis</td>
            </tr>
            <tr>
                <td>8</td>
                <td>Analyst Viewpoint and Conclusion</td>
            </tr>
        </tbody>
    </table>
    """

def figures(keyword, segmentation, regions, players):
    return f"""
    <ul>
        <li>Figure 1: Market Size and Forecast by Region</li>
        <li>Figure 2: Competitive Landscape</li>
        <li>Figure 3: Growth Opportunities by Segment</li>
        <li>Figure 4: Market Dynamics</li>
        <li>Figure 5: Company Profiles</li>
    </ul>
    """

def main():
    st.title("Global TOC Generator")

    st.sidebar.header("Upload Excel File")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type="xls")
    
    if uploaded_file is not None:
        # Load the Excel file
        wb = xlrd.open_workbook(file_contents=uploaded_file.read())
        sheet = wb.sheet_by_index(0)

        st.sidebar.header("Column IDs")
        id_segmentation = st.sidebar.number_input("Segmentation Column ID", min_value=0, value=12)
        id_player = st.sidebar.number_input("Player Column ID", min_value=0, value=8)
        id_keyword = st.sidebar.number_input("Keyword Column ID", min_value=0, value=1)
        id_region = st.sidebar.number_input("Region Column ID", min_value=0, value=5)
        
        regions = st.text_input("Regions", "North America, Eastern Europe, Western Europe, Asia Pacific, Middle East & Africa, South America")
        
        progress_bar = st.progress(0)
        ans_toc = ""
        ans_fig = ""

        for j in range(1, sheet.nrows):
            keyword = sheet.cell_value(j, id_keyword).strip()
            segmentation = sheet.cell_value(j, id_segmentation)
            players = sheet.cell_value(j, id_player)
            regions_input = sheet.cell_value(j, id_region)

            p1 = part1(keyword)
            p1b = part1B(keyword)
            p2 = part2(keyword, segmentation)
            p3a = part3A(keyword, p2[1])
            p3 = part3(keyword, players, p2[2])
            p4 = part4(keyword, regions_input, p3[1]+1, segmentation)
            p5 = part5(keyword, regions_input, p4[1]+1, segmentation)
            p6 = part6(keyword, p5[1])
            
            ans_fig += '"' + table(keyword, segmentation, regions, players) + "<br /><br />"
            ans_fig += figures(keyword, segmentation, regions, players) + '"\n'
            ans_toc += '"' + str(p1) + str(p3a) + str(p1b) + str(p2[0]) + str(p3[0]) + str(p4[0]) + str(p5[0]) + str(p6) + '"\n'
            
            progress_bar.progress((j + 1) / sheet.nrows)

        st.header("Table of Contents")
        st.write(ans_toc)

        st.header("Figures")
        st.write(ans_fig)

        # Create download buttons for the text files
        toc_text = StringIO(ans_toc)
        fig_text = StringIO(ans_fig)
        
        st.download_button(
            label="Download Table of Contents",
            data=toc_text.getvalue(),
            file_name='toc.txt',
            mime='text/plain'
        )
        
        st.download_button(
            label="Download Figures",
            data=fig_text.getvalue(),
            file_name='figures.txt',
            mime='text/plain'
        )

if __name__ == "__main__":
    main()

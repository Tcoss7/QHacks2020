import * as mechanize from 'mechanize';
import {BeautifulSoup} from 'bs4';
import {HTMLSession} from 'requests_html';
import * as re from 're';
import * as requests from 'requests';
import * as csv from 'csv';
import * as pd from 'pandas';
import * as time from 'time';
var corporate_critic_url, df, f, filename, final_ethics_score, product_url;
corporate_critic_url = "http://www.corporatecritic.org/companies.aspx";
function find_company(url) {
    var compName, resp, session, soup, source;
    source = requests.get(url).text;
    soup = new BeautifulSoup(source, "lxml");
    try {
        compName = soup.find({"id": "bylineInfo"}).text;
    } catch(e) {
        session = new HTMLSession();
        resp = session.get(url);
        resp.html.render();
        source = resp.html.html;
        soup = new BeautifulSoup(source, "lxml");
        compName = soup.find({"id": "bylineInfo"}).text;
        console.log(compName);
    }
    return compName;
}
function corporate_critic(companyName) {
    var br, ethicsScore, soup;
    br = new mechanize.Browser();
    br.open(corporate_critic_url);
    br.select_form("Form1");
    br["txtSearch"] = companyName;
    br.submit();
    try {
        soup = new BeautifulSoup(br.response().read(), "html.parser");
        ethicsScore = soup.select_one(".resultlistethiscore").text;
        ethicsScore = re.sub(" ", "", ethicsScore);
        ethicsScore = re.sub(chr(13), "", ethicsScore);
        ethicsScore = re.sub(chr(10), "", ethicsScore);
        ethicsScore = re.sub("\\)", "", ethicsScore);
        ethicsScore = re.sub("\\(", "", ethicsScore);
        console.log(ethicsScore);
    } catch(e) {
        ethicsScore = (- 1);
    }
    return ethicsScore;
}
filename = "Extension/passData.csv";
while (true) {
    time.sleep(2);
    try {
        df = csv.reader(filename);
        product_url = "";
        for (var entry, _pj_c = 0, _pj_a = df, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            entry = _pj_a[_pj_c];
            product_url += entry;
        }
        final_ethics_score = corporate_critic(find_company(product_url));
        f = open(filename, "w+");
        f.close();
    } catch(e) {
        console.log("lol");
    }
}

//# sourceMappingURL=findEthicsScore.js.map

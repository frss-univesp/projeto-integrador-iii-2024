from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
title = "Sistema de emissão de PT"
heading = "Sistema de emissão de PT"

client = MongoClient(r"mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['proj_integrador_ii']
coll = db['perm_trabalho']

def max_pt():
    qt_docs = coll.count_documents({})

    if qt_docs > 0:

        result = coll.aggregate([
            {'$group': {'_id': None, 'max_value': {'$max': '$_id'}}}
        ])
        max_value = int(result.next()['max_value'])
        max_value+=1

    else:
        max_value = 1

    return max_value


@app.route('/', methods=['GET'])
def index():
    pts = coll.find()
    return render_template('index.html', pts=pts)


@app.route('/edit', methods=['GET', 'POST'])
@app.route('/edit/<pt>', methods=['GET', 'POST'])
def edit_pt(pt=None):

    if pt:
        documento = coll.find_one({'_id': int(pt)})
    else:
        documento = None

    return render_template('edit_pt.html', documento=documento)


@app.route('/save_pt', methods=['POST'])
def save_pt():

    if request.method == 'POST':

        nr_pt = request.form.get("_id")
        local = request.form.get("local")
        dt_execucao = request.form.get("dt_execucao")
        dt_conclusao = request.form.get("dt_conclusao")
        dt_prorrog = request.form.get("dt_prorrog")
        descr_ativ = request.form.get("descr_ativ")
        nm_solicte = request.form.get("nm_solicte")
        area_solicte = request.form.get("area_solicte")
        ferram_utilz = request.form.get("ferram_utilz")
        doc_ctrl_risc = request.form.get("ferram_utilz")
        apontamento = request.form.get("apontamento")
        form_ctrl_13 = request.form.get("form_ctrl_13")
        form_ctrl_14 = request.form.get("form_ctrl_14")
        form_ctrl_15 = request.form.get("form_ctrl_15")
        form_ctrl_16 = request.form.get("form_ctrl_16")
        form_ctrl_17 = request.form.get("form_ctrl_17")
        form_ctrl_18 = request.form.get("form_ctrl_18")
        form_ctrl_19 = request.form.get("form_ctrl_19")
        med_adic_ctrl = request.form.get("med_adic_ctrl")
        epi_1 = request.form.get("epi_1")
        epi_2 = request.form.get("epi_2")
        epi_3 = request.form.get("epi_3")
        epi_4 = request.form.get("epi_4")
        epi_5 = request.form.get("epi_5")
        outros_epi = request.form.get("outros_epi")
        epc_1 = request.form.get("epc_1")
        epc_2 = request.form.get("epc_2")
        epc_3 = request.form.get("epc_3")
        epc_4 = request.form.get("epc_4")
        epc_5 = request.form.get("epc_5")
        outros_epc = request.form.get("outros_epc")
        nm_aprovador = request.form.get("nm_aprovador")
        cargo_aprovador = request.form.get("cargo_aprovador")
        dt_aprovacao = request.form.get("dt_aprovacao")
        nm_exec_1 = request.form.get("nm_exec_1")
        cargo_exec_1 = request.form.get("cargo_exec_1")
        nm_exec_2 = request.form.get("nm_exec_2")
        cargo_exec_2 = request.form.get("cargo_exec_2")
        nm_exec_3 = request.form.get("nm_exec_3")
        cargo_exec_3 = request.form.get("cargo_exec_3")
        chk_item1 = True if request.form.get('chk_item1') == 'true' else False
        chk_item2 = True if request.form.get('chk_item2') == 'true' else False
        chk_item3 = True if request.form.get('chk_item3') == 'true' else False
        chk_item4 = True if request.form.get('chk_item4') == 'true' else False
        chk_item5 = True if request.form.get('chk_item5') == 'true' else False
        chk_item5 = True if request.form.get('chk_item5') == 'true' else False
        chk_item6 = True if request.form.get('chk_item6') == 'true' else False
        chk_item7 = True if request.form.get('chk_item7') == 'true' else False
        chk_item8 = True if request.form.get('chk_item8') == 'true' else False
        chk_item9 = True if request.form.get('chk_item9') == 'true' else False
        chk_item10 = True if request.form.get('chk_item10') == 'true' else False
        chk_item11 = True if request.form.get('chk_item11') == 'true' else False
        chk_item12 = True if request.form.get('chk_item12') == 'true' else False
        chk_item13 = True if request.form.get('chk_item13') == 'true' else False
        chk_item14 = True if request.form.get('chk_item14') == 'true' else False
        chk_item15 = True if request.form.get('chk_item15') == 'true' else False
        chk_item16 = True if request.form.get('chk_item16') == 'true' else False
        chk_item17 = True if request.form.get('chk_item17') == 'true' else False
        chk_item18 = True if request.form.get('chk_item18') == 'true' else False
        chk_item19 = True if request.form.get('chk_item19') == 'true' else False

        doc = {
            'local': local,
            'dt_execucao': dt_execucao,
            'dt_conclusao': dt_conclusao,
            'dt_prorrog': dt_prorrog,
            'descr_ativ': descr_ativ,
            'nm_solicte': nm_solicte,
            'area_solicte': area_solicte,
            'ferram_utilz': ferram_utilz,
            'doc_ctrl_risc': doc_ctrl_risc,
            'apontamento': apontamento,
            'chk_item1': chk_item1,
            'chk_item2': chk_item2,
            'chk_item3': chk_item3,
            'chk_item4': chk_item4,
            'chk_item5': chk_item5,
            'chk_item5': chk_item5,
            'chk_item6': chk_item6,
            'chk_item7': chk_item7,
            'chk_item8': chk_item8,
            'chk_item9': chk_item9,
            'chk_item10': chk_item10,
            'chk_item11': chk_item11,
            'chk_item12': chk_item12,
            'chk_item13': chk_item13,
            'form_ctrl_13': form_ctrl_13,
            'chk_item14': chk_item14,
            'form_ctrl_14': form_ctrl_14,
            'chk_item15': chk_item15,
            'form_ctrl_15': form_ctrl_15,
            'chk_item16': chk_item16,
            'form_ctrl_16': form_ctrl_16,
            'chk_item17': chk_item17,
            'form_ctrl_17': form_ctrl_17,
            'chk_item18': chk_item18,
            'form_ctrl_18': form_ctrl_18,
            'chk_item19': chk_item19,
            'form_ctrl_19': form_ctrl_19,
            'med_adic_ctrl': med_adic_ctrl,
            'epi_1': epi_1,
            'epi_2': epi_2,
            'epi_3': epi_3,
            'epi_4': epi_4,
            'epi_5': epi_5,
            'outros_epi': outros_epi,
            'epc_1': epc_1,
            'epc_2': epc_2,
            'epc_3': epc_3,
            'epc_4': epc_4,
            'epc_5': epc_5,
            'outros_epc': outros_epc,
            'nm_aprovador': nm_aprovador,
            'cargo_aprovador': cargo_aprovador,
            'dt_aprovacao': dt_aprovacao,
            'nm_exec_1': nm_exec_1,
            'cargo_exec_1': cargo_exec_1,
            'nm_exec_2': nm_exec_2,
            'cargo_exec_2': cargo_exec_2,
            'nm_exec_3': nm_exec_3,
            'cargo_exec_3': cargo_exec_3            
        }

        if nr_pt:
            coll.update_one({'_id': int(nr_pt)}, {'$set': doc})
        else:
            doc['_id'] = max_pt()
            coll.insert_one(doc)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
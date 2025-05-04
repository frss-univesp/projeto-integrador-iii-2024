import json
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
title = "Sistema de emissão de PT"
heading = "Sistema de emissão de PT"

client = MongoClient(r"mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['proj_integrador_ii']
coll_pt = db['perm_trabalho']
coll_executores = db['executores']
coll_certificacoes = db['certificacoes']

def max_id(collection):
    qt_docs = collection.count_documents({})
    if qt_docs > 0:
        result = collection.aggregate([
            {'$group': {'_id': None, 'max_value': {'$max': '$_id'}}}
        ])
        max_value = int(result.next()['max_value'])
        return max_value + 1
    else:
        return 1

def get_certificacao(cert_id):
    """Busca uma certificação pelo ID."""
    return coll_certificacoes.find_one({'_id': int(cert_id)})

def get_distinct_certificacoes():
    """Busca todas as certificações para o dropdown."""
    return coll_certificacoes.find()


@app.route('/', methods=['GET'])
def index():
    pts = coll_pt.find()
    return render_template('index.html', pts=pts)


@app.route('/edit_pt', methods=['GET', 'POST'])
@app.route('/edit_pt/<pt>', methods=['GET', 'POST'])
def edit_pt(pt=None):
    documento = coll_pt.find_one({'_id': int(pt)}) if pt else None
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
        chk_item1 = True if request.form.get('chk_item1') == 'true' else False
        chk_item2 = True if request.form.get('chk_item2') == 'true' else False
        chk_item3 = True if request.form.get('chk_item3') == 'true' else False
        chk_item4 = True if request.form.get('chk_item4') == 'true' else False
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

        doc_pt = {
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
            'dt_aprovacao': dt_aprovacao
        }

        if nr_pt:
            coll_pt.update_one({'_id': int(nr_pt)}, {'$set': doc_pt})
        else:
            doc_pt['_id'] = max_id(coll_pt)
            coll_pt.insert_one(doc_pt)

        return redirect(url_for('index'))


@app.route('/list_exec', methods=['GET'])
def list_exec():
    executores = coll_executores.find()
    return render_template('list_exec.html', executores=executores)


@app.route('/edit_exec', methods=['GET', 'POST'])
@app.route('/edit_exec/<executor>', methods=['GET', 'POST'])
def edit_exec(executor=None):
    documento = coll_executores.find_one({'_id': int(executor)}) if executor else None
    lista_certificacoes = get_distinct_certificacoes()

    print(documento)

    return render_template('edit_exec.html', documento=documento, lista_certificacoes=lista_certificacoes)


@app.route('/save_exec', methods=['POST'])
def save_exec():
    if request.method == 'POST':
        matricula_str = request.form.get("_id")
        nome_completo = request.form.get('nome_completo')
        data_inclusao_str = request.form.get('data_inclusao')
        data_exclusao_str = request.form.get('data_exclusao')
        funcao = request.form.get('funcao')
        certificacoes_json = request.form.get('certificacoes_json')

        # Convertendo strings de data para o formato adequado para MongoDB
        data_inclusao = data_inclusao_str if data_inclusao_str else None
        data_exclusao = data_exclusao_str if data_exclusao_str else None

        # Agora certificacoes_json contém o array completo de objetos de certificação
        certificacoes = json.loads(certificacoes_json)

        doc_executor_base = {
            'nome_completo': nome_completo,
            'data_inclusao': data_inclusao,
            'data_exclusao': data_exclusao,
            'funcao': funcao,
            'certificacoes': certificacoes
        }

        if matricula_str:
            executor_existente = coll_executores.find_one({'_id': int(matricula_str)})
            if executor_existente and 'certificacoes' in executor_existente:
                # Manter certificações existentes e adicionar novas
                certificacoes_existentes = executor_existente['certificacoes']
                
                # Evitar duplicações baseadas no id_certificacao
                certificacoes_ids_existentes = [cert.get('id_cerficacao') for cert in certificacoes_existentes 
                                            if isinstance(cert, dict) and 'id_cerficacao' in cert]
                
                certificacoes_a_adicionar = [cert for cert in certificacoes 
                                         if cert.get('id_cerficacao') not in certificacoes_ids_existentes]
                
                certificacoes_atualizadas = certificacoes_existentes + certificacoes_a_adicionar
                
                coll_executores.update_one(
                    {'_id': int(matricula_str)},
                    {'$set': {**doc_executor_base, 'certificacoes': certificacoes_atualizadas}}
                )
            else:
                coll_executores.update_one(
                    {'_id': int(matricula_str)},
                    {'$set': doc_executor_base}
                )
        else:
            doc_executor = {**doc_executor_base, '_id': max_id(coll_executores)}
            coll_executores.insert_one(doc_executor)

        return redirect(url_for('list_exec'))


@app.route('/list_certificacoes', methods=['GET'])
def list_certificacoes():
    certificacoes = coll_certificacoes.find()
    return render_template('list_certificacoes.html', certificacoes=certificacoes)


@app.route('/edit_certificacao', methods=['GET', 'POST'])
@app.route('/edit_certificacao/<certificacao>', methods=['GET', 'POST'])
def edit_certificacao(certificacao=None):
    documento = coll_certificacoes.find_one({'_id': int(certificacao)}) if certificacao else None
    return render_template('edit_certificacao.html', documento=documento)


@app.route('/save_certificacao', methods=['POST'])
def save_certificacao():
    if request.method == 'POST':
        id = request.form.get("_id")
        nome_certificacao = request.form.get('nome_certificacao')
        dt_inicio_validade = request.form.get('dt_inicio_validade')
        dt_fim_validade = request.form.get('dt_fim_validade')
        observacao = request.form.get('observacao')
        chk_item1 = True if request.form.get('chk_item1') == 'true' else False
        chk_item2 = True if request.form.get('chk_item2') == 'true' else False
        chk_item3 = True if request.form.get('chk_item3') == 'true' else False
        chk_item4 = True if request.form.get('chk_item4') == 'true' else False
        chk_item5 = True if request.form.get('chk_item5') == 'true' else False
        chk_item6 = True if request.form.get('chk_item6') == 'true' else False
        chk_item7 = True if request.form.get('chk_item7') == 'true' else False
        chk_item8 = True if request.form.get('chk_item8') == 'true' else False
        chk_item9 = True if request.form.get('chk_item9') == 'true' else False
        chk_item10 = True if request.form.get('chk_item10') == 'true' else False
        chk_item11 = True if request.form.get('chk_item11') == 'true' else False
        chk_item12 = True if request.form.get('chk_item12') == 'true' else False

        doc_certificacao = {
            'nome_certificacao': nome_certificacao,
            'dt_inicio_validade': dt_inicio_validade,
            'dt_fim_validade': dt_fim_validade,
            'observacao': observacao,
            'chk_item1': chk_item1,
            'chk_item2': chk_item2,
            'chk_item3': chk_item3,
            'chk_item4': chk_item4,
            'chk_item5': chk_item5,
            'chk_item6': chk_item6,
            'chk_item7': chk_item7,
            'chk_item8': chk_item8,
            'chk_item9': chk_item9,
            'chk_item10': chk_item10,
            'chk_item11': chk_item11,
            'chk_item12': chk_item12
        }

        if id:
            coll_certificacoes.update_one({'_id': int(id)}, {'$set': doc_certificacao})
        else:
            doc_certificacao['_id'] = max_id(coll_certificacoes)
            coll_certificacoes.insert_one(doc_certificacao)

        return redirect(url_for('list_certificacoes'))


if __name__ == '__main__':
    app.run(debug=True)
def diagramm():
    dauer, sportart = data()
    fig = px.pie(values=dauer, names=sportart,
                 labels={"values": "Dauer", "names": "Sportart"},
                 title="Erfasste Sportarten dargestellt nach Sportart und Dauer")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div = plot(fig, output_type="div")
    return div


fig = px.bar(x=["Luca", "Mirjam", "Sarina"], y=[summe_luca, summe_mirjam, summe_sarina])
div = plot(fig, output_type="div")
fig.show()
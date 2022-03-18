heroku pg:psql
\dt


<!-- {% extends "base.html" %}

{% block main %}
{% include 'flash_messages.html' %}
<h1 class="display-5 fw-bold">properties</h1>




<ul>
    {% for pro in properties %}
    
        <div > 
            <li><img  src="{{ url_for('get_image', filename=pro.photo) }}"/></li>
            <li>{{pro.title}}</li>
            <li>{{pro.location}}</li>
            <li>{{pro.price}}</li>
            <li><a href="{{url_for('property_id', propertyid=pro.id)}}">View Property</a></li>
        </div>
    
    
    {% endfor %}   

</ul>
{% endblock %} -->
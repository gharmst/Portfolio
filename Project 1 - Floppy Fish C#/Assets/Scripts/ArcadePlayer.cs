using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// using UnityEngine.SceneManagement;

public class ArcadePlayer : MonoBehaviour
{
    
    // [SerializeField] private float speed;
    public float speed = 2;
    public float velocity = 1;
    private Rigidbody2D body;
    public float force = 300;

    private void Awake()
    {
        body = GetComponent<Rigidbody2D>();
        body.velocity = Vector2.right * speed;
    }

    private void Update()
    {
        // body.velocity = new Vector2(Input.GetAxis("Horizontal") * 0, Input.GetAxis("Vertical") * speed);
        // body.velocity = Vector2.up * velocity;
        if (Input.GetKeyDown(KeyCode.Space))
            body.AddForce(Vector2.up*force);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        print("Colliding");
    }

}
